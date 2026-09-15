import time
import random
import logging
from typing import Callable, TypeVar, Any, Tuple, Type

logger = logging.getLogger("autoclicker.utils")

T = TypeVar("T")

def retry_network_op(
    retries: int = 3,
    backoff_factor: float = 0.5,
    exceptions_to_check: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Decorator that retries a network operation with exponential backoff.
    
    :param retries: Maximum number of retry attempts.
    :param backoff_factor: Multiplier for exponential backoff delay.
    :param exceptions_to_check: Tuple of exceptions that trigger a retry.
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            attempt = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions_to_check as e:
                    attempt += 1
                    if attempt > retries:
                        logger.error(
                            f"Operation '{func.__name__}' failed after {retries} retries. "
                            f"Error: {e}"
                        )
                        raise e
                    
                    # Exponential backoff with jitter
                    delay = backoff_factor * (2 ** (attempt - 1)) + random.uniform(0, 0.1)
                    logger.warning(
                        f"Network exception '{e}' during '{func.__name__}'. "
                        f"Retrying attempt {attempt}/{retries} in {delay:.2f}s..."
                    )
                    time.sleep(delay)
        return wrapper
    return decorator
