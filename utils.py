import functools
import logging
import time
from typing import Any, Callable, Tuple, Type, TypeVar

T = TypeVar("T")
logger = logging.getLogger(__name__)


def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    allowed_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator to retry network requests with exponential backoff."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except allowed_exceptions as err:
                    if attempt == max_retries:
                        logger.error(
                            "Network request '%s' failed after %d retries: %s",
                            func.__name__,
                            max_retries,
                            err,
                        )
                        raise
                    logger.warning(
                        "Attempt %d/%d for '%s' failed (%s). Retrying in %.1fs...",
                        attempt,
                        max_retries,
                        err,
                        current_delay,
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
            raise RuntimeError("Retry limit reached unexpectedly")

        return wrapper

    return decorator
