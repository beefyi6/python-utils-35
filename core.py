import time
import threading
from typing import Callable, Optional

class FastClickEngine:
    """High-performance click timing engine with low-jitter interval control."""

    def __init__(self, click_action: Callable[[], None], interval: float = 0.01):
        self.click_action = click_action
        self.interval = max(0.001, interval)
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._clicks_count = 0

    def start(self) -> None:
        """Start the click execution loop in a background thread."""
        if self._running:
            return
        self._running = True
        self._clicks_count = 0
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop the click execution thread."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _run_loop(self) -> None:
        """Optimized execution loop using perf_counter to minimize drift."""
        next_time = time.perf_counter()
        
        while self._running:
            now = time.perf_counter()
            if now >= next_time:
                self.click_action()
                self._clicks_count += 1
                # Prevent cumulative timing drift by adding to target schedule
                next_time += self.interval
            else:
                sleep_time = next_time - now
                # Use hybrid sleep/spin for low latency without high CPU spike
                if sleep_time > 0.002:
                    time.sleep(sleep_time - 0.001)

    @property
    def clicks_count(self) -> int:
        return self._clicks_count
