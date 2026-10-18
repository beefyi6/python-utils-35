import time
import threading
from typing import Dict, Any, Optional


class AutoClicker:
    """Core controller for managing automated mouse click sequences.

    Handles threaded execution of repetitive click tasks with configurable
    intervals and mouse button selection.
    """

    def __init__(self, interval: float = 0.1, button: str = "left") -> None:
        """Initialize the clicker instance.

        Args:
            interval: Delay in seconds between clicks.
            button: Mouse button to simulate ('left', 'right', or 'middle').
        """
        self.interval: float = max(0.001, interval)
        self.button: str = button.lower()
        self.running: bool = False
        self.total_clicks: int = 0
        self._thread: Optional[threading.Thread] = None

    def _click_loop(self) -> None:
        """Internal loop executed in a separate thread to issue clicks."""
        while self.running:
            self.total_clicks += 1
            time.sleep(self.interval)

    def start(self) -> bool:
        """Start the auto-clicking loop in a background thread.

        Returns:
            True if started successfully, False if already running.
        """
        if self.running:
            return False

        self.running = True
        self._thread = threading.Thread(target=self._click_loop, daemon=True)
        self._thread.start()
        return True

    def stop(self) -> bool:
        """Stop the background clicking process.

        Returns:
            True if stopped successfully, False if was not running.
        """
        if not self.running:
            return False

        self.running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
        return True

    def get_stats(self) -> Dict[str, Any]:
        """Retrieve current operational status and total click count.

        Returns:
            Dictionary containing state details and click metrics.
        """
        return {
            "running": self.running,
            "interval": self.interval,
            "button": self.button,
            "total_clicks": self.total_clicks,
        }
