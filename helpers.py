import time
import random
import pyautogui

def safe_click(x: int, y: int, interval: float = 0.1):
    """Move mouse to coordinates and perform a click."""
    pyautogui.moveTo(x, y)
    time.sleep(interval)
    pyautogui.click()

def random_delay(min_sec: float, max_sec: float):
    """Sleep for a random duration between specified bounds."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

def get_screen_center():
    """Return the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def drag_to(start_x: int, start_y: int, end_x: int, end_y: int, duration: float = 0.5):
    """Perform a smooth drag operation between two points."""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=duration, button='left')

def is_pixel_color(x: int, y: int, target_rgb: tuple, tolerance: int = 10):
    """Check if pixel at location matches target RGB within tolerance."""
    current_color = pyautogui.pixel(x, y)
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(current_color, target_rgb))