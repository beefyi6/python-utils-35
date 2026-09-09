import time
import pyautogui
from typing import Tuple, Optional

class ClickHandler:
    """Handles automated mouse clicking operations with safety delays."""

    def __init__(self, interval: float = 0.1, button: str = 'left') -> None:
        """Initialize handler with click configuration."""
        self.interval: float = interval
        self.button: str = button

    def execute_click(self, coordinates: Tuple[int, int]) -> bool:
        """Perform a single click at the specified screen coordinates."""
        try:
            x, y = coordinates
            pyautogui.click(x=x, y=y, button=self.button)
            time.sleep(self.interval)
            return True
        except (pyautogui.FailSafeException, Exception):
            return False

    def execute_sequence(self, positions: list[Tuple[int, int]]) -> int:
        """Perform a sequence of clicks across multiple coordinates."""
        success_count: int = 0
        for pos in positions:
            if self.execute_click(pos):
                success_count += 1
        return success_count

    def get_current_position(self) -> Tuple[int, int]:
        """Retrieve the current mouse cursor location."""
        x, y = pyautogui.position()
        return (int(x), int(y))