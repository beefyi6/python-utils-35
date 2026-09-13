import time
import sys

def precise_sleep(duration: float) -> None:
    """
    Suspends execution with high precision for the specified duration.
    Combines standard sleep with spin-locking for sub-millisecond accuracy.
    """
    if duration <= 0:
        return
        
    start_time = time.perf_counter()
    target_time = start_time + duration
    
    # Use standard sleep for the bulk of the duration to save CPU
    remaining = duration
    while remaining > 0.015:
        time.sleep(remaining - 0.01)
        remaining = target_time - time.perf_counter()
        
    # Active spin-locking for high-precision remainder
    while time.perf_counter() < target_time:
        pass

def calculate_intervals(clicks_per_second: float) -> float:
    """
    Calculates the exact delay interval needed between clicks.
    """
    if clicks_per_second <= 0:
        return 0.1
    return 1.0 / clicks_per_second