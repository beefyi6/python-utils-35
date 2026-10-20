import time
import urllib.request
import urllib.error
import logging
from functools import wraps
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_op(
    max_retries: int = 3,
    delay: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (urllib.error.URLError, TimeoutError, OSError)
) -> Callable:
    """Decorator that retries network operations with exponential backoff."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    if attempt == max_retries:
                        logger.error("Network operation failed after %d attempts: %s", max_retries, err)
                        raise
                    logger.warning(
                        "Attempt %d/%d failed (%s). Retrying in %.1fs...",
                        attempt, max_retries, err, current_delay
                    )
                    time.sleep(current_delay)
                    current_delay *= backoff_factor
        return wrapper
    return decorator


@retry_network_op(max_retries=3, delay=0.5)
def fetch_remote_config(url: str, timeout: float = 5.0) -> bytes:
    """Fetch remote autoclicker profile or update configuration."""
    req = urllib.request.Request(url, headers={"User-Agent": "AutoClicker-Utils/3.5"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()
