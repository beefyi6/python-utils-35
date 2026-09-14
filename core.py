import time
import threading
from typing import Callable, Optional

class ClickEngine:
    """Core autoclicker engine optimized for high-precision timing."""

    def __init__(self, interval: float = 0.01) -> None:
        self.interval = max(0.001, interval)
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self._callback: Optional[Callable[[], None]] = None

    def set_callback(self, callback: Callable[[], None]) -> None:
        self._callback = callback

    def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)

    def _run_loop(self) -> None:
        next_time = time.perf_counter()
        while self._running:
            if self._callback:
                self._callback()
            next_time += self.interval
            sleep_time = next_time - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:
                next_time = time.perf_counter()
