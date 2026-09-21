import time
import threading
from typing import Optional

class ClickHandler:
    """Manages execution state and timing for autoclicker tasks."""
    def __init__(self, interval: float = 0.1):
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def start(self) -> None:
        """Starts the execution loop if not already running."""
        with self._lock:
            if not self.running:
                self.running = True
                threading.Thread(target=self._run_loop, daemon=True).start()

    def stop(self) -> None:
        """Signals the execution loop to terminate."""
        with self._lock:
            self.running = False

    def _run_loop(self) -> None:
        """Internal loop executing click actions."""
        while self.running:
            self._perform_click()
            time.sleep(self.interval)

    def _perform_click(self) -> None:
        """Placeholder for low-level click injection logic."""
        # Integration point for system input libraries
        pass

    def update_interval(self, new_interval: float) -> None:
        """Updates the click rate dynamically."""
        self.interval = max(0.01, new_interval)