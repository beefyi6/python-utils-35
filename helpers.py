import time
import logging
import functools
from typing import Callable, Any, Type, Tuple

logger = logging.getLogger("autoclicker.helpers")


def retry_network_op(
    max_retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    """Decorator that retries network operations with exponential backoff.

    Useful for autoclicker preset sync, cloud config fetching, and license checks.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    retries += 1
                    if retries >= max_retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {max_retries} attempts: {err}"
                        )
                        raise

                    sleep_time = backoff_factor * (2 ** (retries - 1))
                    logger.warning(
                        f"Attempt {retries}/{max_retries} for '{func.__name__}' failed: {err}. "
                        f"Retrying in {sleep_time:.2f}s..."
                    )
                    time.sleep(sleep_time)
        return wrapper
    return decorator
