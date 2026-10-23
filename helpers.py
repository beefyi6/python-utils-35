import time
import threading
from typing import Callable, Any

class ClickOptimizer:
    """
    High-frequency execution handler to minimize overhead
    during tight autoclicker loops.
    """
    def __init__(self, interval: float):
        self.interval = interval
        self._last_time = time.perf_counter()

    def optimized_wait(self) -> None:
        """
        Reduces CPU busy-waiting using adaptive sleep.
        """
        elapsed = time.perf_counter() - self._last_time
        remaining = self.interval - elapsed
        if remaining > 0.002:
            time.sleep(remaining - 0.001)
        
        # Spin lock for sub-millisecond precision
        while time.perf_counter() - self._last_time < self.interval:
            pass
        
        self._last_time = time.perf_counter()

def batch_process(func: Callable, count: int) -> None:
    """
    Execution of rapid actions in thread-safe batches
    to reduce context switching overhead.
    """
    for _ in range(count):
        func()

def get_high_res_timestamp() -> float:
    """
    Wrapper for performance counter providing monotonic timing
    data for interval tracking.
    """
    return time.perf_counter()