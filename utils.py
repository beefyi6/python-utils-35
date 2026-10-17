import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_network_op(retries=3, delay=1, backoff=2):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    if attempt == retries - 1:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Attempt {attempt + 1} failed, retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

@retry_network_op(retries=3, delay=2)
def fetch_remote_config(url):
    """Example network operation for autoclicker configuration."""
    # Simulating network call
    print(f"Fetching configuration from {url}")
    raise ConnectionError("Server unreachable")