import time
import threading
import pyautogui

class ClickHandler:
    """Handles click operations with thread-safe execution."""

    def __init__(self, interval: float = 0.01):
        self.interval = interval
        self._running = False
        self._lock = threading.Lock()
        # Disable pyautogui failsafe for raw performance optimization
        pyautogui.FAILSAFE = False

    def start_clicking(self) -> None:
        with self._lock:
            self._running = True
        threading.Thread(target=self._run_loop, daemon=True).start()

    def stop_clicking(self) -> None:
        with self._lock:
            self._running = False

    def _run_loop(self) -> None:
        """High-frequency click loop with minimal overhead."""
        click_func = pyautogui.click
        while True:
            with self._lock:
                if not self._running:
                    break
            
            click_func()
            
            if self.interval > 0:
                time.sleep(self.interval)

    def update_interval(self, new_interval: float) -> None:
        with self._lock:
            self.interval = new_interval