import logging
import pyautogui
import time

logger = logging.getLogger(__name__)

def safe_click(x: int, y: int, interval: float = 0.1) -> bool:
    """Performs a click with boundary and coordinate validation."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            logger.error(f"Coordinates ({x}, {y}) out of screen bounds")
            return False
            
        pyautogui.click(x, y)
        time.sleep(interval)
        return True
        
    except pyautogui.FailSafeException:
        logger.warning("Fail-safe triggered: mouse moved to corner")
        return False
    except pyautogui.PyAutoGUIException as e:
        logger.error(f"PyAutoGUI internal error: {e}")
        return False
    except Exception as e:
        logger.exception(f"Unexpected error during click event: {e}")
        return False

def validate_interval(value: float) -> float:
    """Ensures click interval is within practical safety limits."""
    try:
        interval = float(value)
        if interval < 0.01:
            logger.warning("Interval too low, clamping to 0.01s")
            return 0.01
        return interval
    except (ValueError, TypeError):
        logger.error("Invalid interval format, defaulting to 0.5s")
        return 0.5