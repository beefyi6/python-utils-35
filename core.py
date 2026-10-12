import time
from typing import Callable, Optional

class OptimizedClickEngine:
    """High-precision click scheduling engine with drift compensation."""

    def __init__(self, click_func: Callable[[], None], interval: float = 0.001):
        self.click_func = click_func
        self.interval = max(0.0001, interval)
        self._is_running = False
        self._total_clicks = 0

    def start(self, duration: Optional[float] = None) -> int:
        """Execute click loop with microsecond-level timing optimization."""
        self._is_running = True
        self._total_clicks = 0
        start_time = time.perf_counter()
        next_click_time = start_time

        while self._is_running:
            current_time = time.perf_counter()

            if duration and (current_time - start_time) >= duration:
                break

            if current_time >= next_click_time:
                self.click_func()
                self._total_clicks += 1
                next_click_time += self.interval

                # Catch up if execution falls significantly behind schedule
                if current_time - next_click_time > self.interval * 5:
                    next_click_time = current_time + self.interval

            # Hybrid spin-wait optimization for low CPU load with high precision
            sleep_time = next_click_time - time.perf_counter()
            if sleep_time > 0.002:
                time.sleep(sleep_time - 0.001)

        self._is_running = False
        return self._total_clicks

    def stop(self) -> None:
        """Signal the click engine to terminate the execution loop."""
        self._is_running = False
