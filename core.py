import time
import urllib.request
import urllib.error
import random
import logging

logger = logging.getLogger("autoclicker.core")

def retry_on_failure(retries=3, backoff_factor=1.5, exceptions=(urllib.error.URLError, OSError)):
    """
    Decorator to retry network operations with exponential backoff and jitter.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            delay = 1.0
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        logger.error(f"Network operation failed permanently after {retries} attempts: {e}")
                        raise e
                    
                    # Apply backoff with random jitter to prevent thundering herd problem
                    jitter = random.uniform(0.1, 0.5)
                    sleep_time = (delay * backoff_factor) + jitter
                    logger.warning(
                        f"Attempt {attempt} failed: {e}. Retrying in {sleep_time:.2f} seconds..."
                    )
                    time.sleep(sleep_time)
                    delay = sleep_time
        return wrapper
    return decorator

@retry_on_failure(retries=4, backoff_factor=2.0)
def fetch_remote_config(url: str) -> str:
    """
    Fetches the autoclicker profiles or configuration updates from a remote coordinator.
    """
    headers = {"User-Agent": "Autoclicker-Utils/3.5 (NetworkClient)"}
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=5) as response:
        return response.read().decode("utf-8")
