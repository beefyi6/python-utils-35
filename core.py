import time
import threading
from typing import Callable

class ClickEngine:
    """High-performance autoclicker engine utilizing event polling."""
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def start_clicking(self, action: Callable[[], None]) -> None:
        """Executes action loop with high-precision timing."""
        self.running = True
        last_time = time.perf_counter()

        while self.running:
            # Use performance counter for sub-millisecond accuracy
            current_time = time.perf_counter()
            elapsed = current_time - last_time
            
            if elapsed >= self.interval:
                action()
                last_time = current_time
            else:
                # Yield CPU slightly to prevent thread starvation
                time.sleep(max(0, self.interval - elapsed) * 0.5)

    def stop(self) -> None:
        """Graceful shutdown of engine execution."""
        with self._lock:
            self.running = False

# Optimized configuration constants
POLLING_RATE_LIMIT = 0.001
THREAD_SAFETY_ENABLED = True