import time
import threading
import pyautogui

class ClickProcessor:
    """Handles autonomous mouse click execution tasks."""

    def __init__(self, interval=0.1):
        self.interval = interval
        self._running = False
        self._thread = None

    def start(self):
        """Starts the background clicking loop."""
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._run_loop, daemon=True)
            self._thread.start()

    def stop(self):
        """Signals the background thread to stop."""
        self._running = False
        if self._thread:
            self._thread.join()

    def _run_loop(self):
        """Internal loop for continuous clicking operations."""
        while self._running:
            pyautogui.click()
            time.sleep(self.interval)

    def update_interval(self, new_interval):
        """Updates the click frequency safely."""
        if new_interval > 0:
            self.interval = new_interval

if __name__ == "__main__":
    # Example usage for demonstration
    processor = ClickProcessor(interval=0.5)
    processor.start()
    try:
        time.sleep(5)
    finally:
        processor.stop()