import pyautogui
import time
from typing import Tuple

def perform_click(x: int, y: int, interval: float = 0.01) -> None:
    """Execute a single mouse click at specified coordinates."""
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(interval)

def drag_element(start: Tuple[int, int], end: Tuple[int, int], duration: float = 0.5) -> None:
    """Execute a drag operation from start point to end point."""
    pyautogui.moveTo(start[0], start[1])
    pyautogui.dragTo(end[0], end[1], duration=duration, button='left')

def safety_check(x: int, y: int, screen_size: Tuple[int, int]) -> bool:
    """Validate coordinates against current screen dimensions."""
    width, height = screen_size
    return 0 <= x <= width and 0 <= y <= height

def click_sequence(coords: list, delay: float) -> None:
    """Iterate through list of coordinates and click each."""
    for x, y in coords:
        perform_click(x, y, delay)

def get_mouse_position() -> Tuple[int, int]:
    """Retrieve current cursor screen coordinates."""
    return pyautogui.position()