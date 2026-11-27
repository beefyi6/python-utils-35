import time
import random
import pyautogui
from typing import Tuple

def get_random_delay(min_ms: int, max_ms: int) -> float:
    """Calculates random delay between clicks to mimic human behavior."""
    return random.uniform(min_ms / 1000, max_ms / 1000)

def perform_click(x: int, y: int, button: str = 'left') -> None:
    """Executes a click at specific coordinates."""
    pyautogui.click(x=x, y=y, button=button)

def get_mouse_position() -> Tuple[int, int]:
    """Returns the current screen coordinates of the mouse."""
    return pyautogui.position()

def safe_sleep(seconds: float) -> None:
    """Sleeps for a given time duration."""
    if seconds > 0:
        time.sleep(seconds)

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are within primary screen bounds."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height