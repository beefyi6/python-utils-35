import pyautogui
import time

def click_at(x, y):
    """Simulates a mouse click at the specified coordinates."""
    pyautogui.click(x, y)


def double_click_at(x, y):
    """Simulates a double mouse click at the specified coordinates."""
    pyautogui.doubleClick(x, y)


def hold_mouse(x, y, duration):
    """Holds the mouse button down at the specified coordinates for a duration."""
    pyautogui.mouseDown(x, y)
    time.sleep(duration)
    pyautogui.mouseUp()


def move_mouse(x, y, duration=0.25):
    """Moves the mouse to the specified coordinates over a given duration."""
    pyautogui.moveTo(x, y, duration)


def drag_mouse_to(x, y, duration=0.5):
    """Drags the mouse to the specified coordinates over a duration."""
    pyautogui.dragTo(x, y, duration)


def wait(seconds):
    """Pauses execution for a specified amount of seconds."""
    time.sleep(seconds)
