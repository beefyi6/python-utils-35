import functools
import random
import time
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger("autoclicker.utils")

def retry_network_op(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (ConnectionError, TimeoutError)
) -> Callable:
    """
    Decorator implementing exponential backoff with jitter for network calls.
    Ensures transient network drops during autoclicker tasks don't cause crashes.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            delay = initial_delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_retries:
                        logger.error(f"Failed after {max_retries} attempts: {exc}")
                        raise exc
                    
                    # Apply jitter to mitigate colliding retries
                    jitter = random.uniform(0.1, 0.5)
                    sleep_time = (delay * backoff_factor) + jitter
                    
                    logger.warning(
                        f"Network operation failed: {exc}. Retrying in {sleep_time:.2f}s "
                        f"(Attempt {attempt}/{max_retries})"
                    )
                    time.sleep(sleep_time)
                    delay = sleep_time
            return func(*args, **kwargs)
        return wrapper
    return decorator