import time
import pyautogui
from typing import Tuple, Optional

def perform_click(x: int, y: int, interval: float = 0.01) -> bool:
    """
    Executes a mouse click at specified coordinates.

    Args:
        x: Horizontal screen coordinate.
        y: Vertical screen coordinate.
        interval: Time duration to sleep after clicking.

    Returns:
        bool: True if click was successful, False otherwise.
    """
    try:
        pyautogui.click(x=x, y=y)
        time.sleep(interval)
        return True
    except Exception:
        return False

def get_screen_center() -> Tuple[int, int]:
    """
    Retrieves the center coordinates of the primary display.

    Returns:
        Tuple[int, int]: The (x, y) coordinates of the center.
    """
    width, height = pyautogui.size()
    return (width // 2, height // 2)

def validate_coordinates(x: int, y: int) -> bool:
    """
    Checks if coordinates are within screen boundaries.

    Args:
        x: Screen X position.
        y: Screen Y position.

    Returns:
        bool: True if coordinates are valid, False otherwise.
    """
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height