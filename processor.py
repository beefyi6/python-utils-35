import time
import threading
from typing import Optional, Callable

class ClickProcessor:
    """Handles the execution of autoclick events in a separate thread."""

    def __init__(self, interval: float = 0.1) -> None:
        self.interval: float = interval
        self._running: bool = False
        self._thread: Optional[threading.Thread] = None

    def start(self, action_callback: Callable[[], None]) -> None:
        """Starts the click loop execution."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(
                target=self._run_loop, 
                args=(action_callback,),
                daemon=True
            )
            self._thread.start()

    def stop(self) -> None:
        """Stops the click loop execution."""
        self._running = False
        if self._thread is not None:
            self._thread.join()
            self._thread = None

    def _run_loop(self, callback: Callable[[], None]) -> None:
        """Internal loop to execute actions at set intervals."""
        while self._running:
            callback()
            time.sleep(self.interval)

    def update_interval(self, new_interval: float) -> None:
        """Adjusts the frequency of click events."""
        self.interval = max(0.01, new_interval)