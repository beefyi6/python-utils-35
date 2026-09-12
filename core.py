import time
import pyautogui
import random

def safe_click(x, y, interval=0.1):
    """Perform a mouse click at coordinates with a small delay."""
    pyautogui.moveTo(x, y)
    time.sleep(interval)
    pyautogui.click()

def random_jitter(x, y, radius=5):
    """Add slight human-like randomization to click coordinates."""
    x_offset = random.randint(-radius, radius)
    y_offset = random.randint(-radius, radius)
    return x + x_offset, y + y_offset

def perform_sequence(coordinates, delay=1.0):
    """Execute a series of clicks based on a list of tuples."""
    for x, y in coordinates:
        jx, jy = random_jitter(x, y)
        safe_click(jx, jy)
        time.sleep(delay)

def get_screen_center():
    """Return the center coordinates of the primary display."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def emergency_stop_check():
    """Check for mouse at top-left corner as kill switch."""
    x, y = pyautogui.position()
    if x == 0 and y == 0:
        raise InterruptedError("Emergency stop triggered at origin")

if __name__ == "__main__":
    # Example usage for autoclicker functionality
    print("Starting click sequence...")
    try:
        center = get_screen_center()
        perform_sequence([center, center])
    except InterruptedError as e:
        print(e)