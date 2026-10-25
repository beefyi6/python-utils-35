import time
import threading
from typing import Callable

class ClickEngine:
    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def start_optimized_loop(self, action_callback: Callable[[], None]) -> None:
        """Executes clicks using high-resolution sleep adjustment."""
        self.running = True
        last_time = time.perf_counter()
        
        while self.running:
            action_callback()
            
            # Calculate precise drift-corrected sleep time
            elapsed = time.perf_counter() - last_time
            sleep_time = max(0, self.interval - elapsed)
            
            if sleep_time > 0.001:
                time.sleep(sleep_time)
            
            last_time = time.perf_counter()

    def stop(self) -> None:
        with self._lock:
            self.running = False

    def update_frequency(self, new_interval: float) -> None:
        with self._lock:
            self.interval = new_interval