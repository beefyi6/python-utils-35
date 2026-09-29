import time
import pyautogui
from typing import Tuple, Optional

class ClickHandler:
    """Handles mouse automation logic for the autoclicker."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize handler with click interval in seconds."""
        self.interval: float = interval
        self.is_running: bool = False

    def execute_click(self, x: int, y: int) -> None:
        """Perform a single click at specified screen coordinates."""
        pyautogui.click(x=x, y=y)

    def start_loop(self, coords: Tuple[int, int], duration: Optional[float] = None) -> None:
        """
        Execute continuous clicks until stop requested or duration elapsed.
        :param coords: (x, y) target coordinates
        :param duration: optional timeout in seconds
        """
        self.is_running = True
        start_time: float = time.time()

        while self.is_running:
            if duration and (time.time() - start_time) > duration:
                break
            
            self.execute_click(*coords)
            time.sleep(self.interval)

    def stop_loop(self) -> None:
        """Terminate the ongoing click loop."""
        self.is_running = False