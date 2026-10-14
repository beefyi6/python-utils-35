import logging
import pyautogui
import time

logger = logging.getLogger(__name__)

def execute_click(x: int, y: int, interval: float = 0.1):
    """Performs a mouse click with input validation and safety checks."""
    try:
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError(f"Coordinates must be integers, got ({type(x)}, {type(y)})")
        
        screen_width, screen_height = pyautogui.size()
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")
            
        # Fail-safe: move mouse to top-left to abort
        pyautogui.FAILSAFE = True
        
        pyautogui.click(x, y)
        time.sleep(interval)
        
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered: process aborted by user")
        raise
    except pyautogui.PyAutoGUIException as e:
        logger.error(f"PyAutoGUI interaction error: {e}")
    except ValueError as e:
        logger.warning(f"Invalid click parameters: {e}")
    except Exception as e:
        logger.critical(f"Unexpected system error during click: {e}")

def batch_click_process(coords_list):
    """Processes a list of coordinate tuples with error isolation."""
    for coords in coords_list:
        try:
            execute_click(*coords)
        except (ValueError, TypeError) as e:
            logger.error(f"Skipping invalid coordinate entry {coords}: {e}")
            continue