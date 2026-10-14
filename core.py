import time
import pyautogui
from typing import Tuple, Optional

class AutoClicker:
    """Handles automated clicking operations for the application."""

    def __init__(self, interval: float = 0.1) -> None:
        """Initialize the clicker with a specified delay."""
        self.interval: float = interval
        self.running: bool = False

    def perform_click(self, coords: Optional[Tuple[int, int]] = None) -> None:
        """
        Execute a mouse click at current position or specified coordinates.
        
        :param coords: Optional (x, y) tuple for destination.
        """
        if coords:
            pyautogui.click(coords[0], coords[1])
        else:
            pyautogui.click()
        time.sleep(self.interval)

    def run_sequence(self, duration: int, coords: Optional[Tuple[int, int]] = None) -> None:
        """
        Run a burst of clicks for a set duration.
        
        :param duration: Seconds to run the sequence.
        :param coords: Optional (x, y) target coordinates.
        """
        self.running = True
        end_time: float = time.time() + duration
        
        while self.running and time.time() < end_time:
            self.perform_click(coords)
        
        self.running = False

    def stop(self) -> None:
        """Halt the current clicker operation."""
        self.running = False