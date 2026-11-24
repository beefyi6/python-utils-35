import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry_operation(retries=3, delay=1.0, backoff=2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_retries = retries
            current_delay = delay
            
            while current_retries > 0:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    current_retries -= 1
                    if current_retries == 0:
                        logger.error(f"Final attempt failed for {func.__name__}")
                        raise
                    
                    logger.warning(f"Retry {retries - current_retries}/{retries} for {func.__name__}: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2.0)
def perform_network_request(request_func, *args):
    """Example usage wrapper for network tasks."""
    return request_func(*args)