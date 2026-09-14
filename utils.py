import pyautogui
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def perform_click(x: int, y: int, interval: float = 0.1) -> bool:
    """Performs a safe click operation with boundary checking."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            logger.error(f"Coordinates ({x}, {y}) outside screen bounds.")
            return False
            
        pyautogui.click(x, y)
        time.sleep(max(0, interval))
        return True
        
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered by user.")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during click: {e}")
        return False

def validate_coordinates(coords: tuple) -> bool:
    """Ensures coordinates are valid numeric types."""
    if not isinstance(coords, tuple) or len(coords) != 2:
        return False
    return all(isinstance(i, (int, float)) for i in coords)

if __name__ == "__main__":
    # Example usage with validation
    target = (100, 200)
    if validate_coordinates(target):
        perform_click(*target)
    else:
        logger.warning("Invalid coordinate format provided.")