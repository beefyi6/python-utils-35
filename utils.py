import time
import functools
import logging

# Logger setup for autoclicker operations
logger = logging.getLogger('python-utils-35')

def retry_network_operation(max_retries=3, delay=1.0):
    """
    Decorator to implement exponential backoff retry logic 
    for unstable network-dependent autoclicker endpoints.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_retries:
                        logger.error(f"Final attempt failed for {func.__name__}: {e}")
                        raise
                    
                    logger.warning(f"Retry {attempts}/{max_retries} for {func.__name__} after {current_delay}s")
                    time.sleep(current_delay)
                    current_delay *= 2
            return None
        return wrapper
    return decorator