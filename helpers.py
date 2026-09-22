import time
import pyautogui
import random

def safe_click(x, y, interval=0.1):
    """Performs a click with a randomized delay to avoid detection."""
    pyautogui.moveTo(x, y)
    time.sleep(random.uniform(0.05, interval))
    pyautogui.click()

def drag_to(x1, y1, x2, y2, duration=0.5):
    """Executes a mouse drag operation between two points."""
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, duration=duration, button='left')

def get_screen_center():
    """Calculates the center of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def human_pause(min_sec=0.5, max_sec=2.0):
    """Introduces a random delay to simulate human behavior."""
    time.sleep(random.uniform(min_sec, max_sec))

def validate_bounds(x, y):
    """Ensures coordinates are within screen dimensions."""
    width, height = pyautogui.size()
    return 0 <= x < width and 0 <= y < height