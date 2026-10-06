import time
import functools
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def retry_network_operation(max_retries: int = 3, delay: float = 1.0):
    """
    Decorator to retry network-bound operations on failure.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
            
            logger.error(f"Operation failed after {max_retries} attempts.")
            raise last_exception
        return wrapper
    return decorator

def validate_connection(target_url: str) -> bool:
    """
    Basic connectivity check helper for the autoclicker environment.
    """
    import socket
    try:
        host = target_url.replace("https://", "").replace("http://", "").split("/")[0]
        socket.create_connection((host, 80), timeout=5)
        return True
    except (OSError, socket.timeout):
        return False