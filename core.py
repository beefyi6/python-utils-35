import time
import pyautogui
from typing import Tuple

def safe_click(x: int, y: int, interval: float = 0.1) -> None:
    """Performs a click at specified coordinates with a brief delay."""
    pyautogui.moveTo(x, y)
    time.sleep(interval)
    pyautogui.click()

def get_screen_center() -> Tuple[int, int]:
    """Calculates the center point of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def perform_macro(coords: list, iterations: int = 1) -> None:
    """Executes a sequence of clicks for a defined number of cycles."""
    for _ in range(iterations):
        for x, y in coords:
            safe_click(x, y)
            time.sleep(0.05)

def validate_bounds(x: int, y: int) -> bool:
    """Checks if coordinates are within screen resolution limits."""
    width, height = pyautogui.size()
    return 0 <= x <= width and 0 <= y <= height

if __name__ == '__main__':
    # Example usage for automated clicking sequence
    center = get_screen_center()
    if validate_bounds(*center):
        perform_macro([center], iterations=3)