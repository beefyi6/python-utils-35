import time
import random
from functools import wraps

def retry_network_operation(max_retries: int = 3, initial_delay: float = 1.0, backoff_factor: float = 2.0):
    """Decorator that adds retry logic for network operations. Retries on common network exceptions with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            delay = initial_delay
            while attempt <= max_retries:
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError, OSError) as exc:
                    attempt += 1
                    if attempt > max_retries:
                        raise
                    # Add jitter to avoid thundering herd
                    jitter = random.uniform(0, 0.1) * delay
                    time.sleep(delay + jitter)
                    delay *= backoff_factor
            # Unreachable
            raise RuntimeError("Retry logic error")
        return wrapper
    return decorator

# Example usage in context of utility for network calls
@retry_network_operation(max_retries=4, initial_delay=0.2)
def perform_network_request(endpoint: str, payload: dict = None) -> dict:
    """Placeholder for actual network call, e.g., using requests or urllib. This would typically be an HTTP POST or GET."""
    # Simulate variable network reliability
    if random.random() < 0.8:
        # Simulate success
        return {"result": "ok", "endpoint": endpoint}
    else:
        # Simulate failure
        raise ConnectionError(f"Failed to connect to {endpoint}")

def with_retry(max_retries: int = 3):
    """Alternative simple retry wrapper."""
    def inner(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            for i in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if i == max_retries - 1:
                        raise
                    time.sleep(1)
            return None
        return wrapped
    return inner