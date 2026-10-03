import time
import threading
from typing import Callable, Optional

class ClickHandler:
    """Handles the execution of mouse click events."""

    def __init__(self, interval: float = 0.1) -> None:
        self.interval: float = interval
        self.is_running: bool = False
        self._thread: Optional[threading.Thread] = None

    def start(self, click_action: Callable[[], None]) -> None:
        """Starts the background click loop."""
        if not self.is_running:
            self.is_running = True
            self._thread = threading.Thread(target=self._run, args=(click_action,), daemon=True)
            self._thread.start()

    def stop(self) -> None:
        """Stops the background click loop."""
        self.is_running = False
        if self._thread:
            self._thread.join()

    def _run(self, click_action: Callable[[], None]) -> None:
        """Internal loop for continuous clicking."""
        while self.is_running:
            click_action()
            time.sleep(self.interval)

    def set_interval(self, interval: float) -> None:
        """Updates the delay between clicks."""
        self.interval = max(0.01, interval)