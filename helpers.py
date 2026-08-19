import time
import pyautogui


def click_mouse(x, y):
    """Clicks the mouse at the given coordinates."""
    pyautogui.click(x, y)


def wait(seconds):
    """Waits for a specified number of seconds."""
    time.sleep(seconds)


def move_mouse(x, y, duration=0.5):
    """Moves the mouse to the specified coordinates over the given duration."""
    pyautogui.moveTo(x, y, duration)


def double_click_mouse(x, y):
    """Performs a double click at the given coordinates."""
    pyautogui.doubleClick(x, y)


def type_text(text):
    """Types the given text."""
    pyautogui.typewrite(text)


def wait_image(image_path, timeout=30):
    """Waits for an image to appear on the screen or times out."""
    start_time = time.time()
    while True:
        if pyautogui.locateOnScreen(image_path):
            return True
        if time.time() - start_time > timeout:
            return False
        time.sleep(0.5)