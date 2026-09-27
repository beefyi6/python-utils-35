import time
import logging
import pyautogui

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('autoclicker')

def perform_click(x: int, y: int, interval: float):
    """Executes mouse click with coordinate and boundary validation."""
    try:
        screen_width, screen_height = pyautogui.size()
        
        if not (0 <= x <= screen_width and 0 <= y <= screen_height):
            raise ValueError(f"Coordinates ({x}, {y}) out of screen bounds")
            
        if interval < 0:
            raise ValueError("Click interval must be a non-negative number")

        pyautogui.click(x, y)
        time.sleep(interval)
        
    except pyautogui.FailSafeException:
        logger.error("Fail-safe triggered: stopping clicker")
        raise
    except ValueError as e:
        logger.error(f"Invalid input parameters: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during click execution: {e}")

def run_autoclicker(target_coords: list, iterations: int, delay: float):
    """Orchestrates multiple clicks with iteration safety."""
    if not target_coords:
        logger.warning("No coordinates provided for clicking")
        return

    for i in range(iterations):
        for x, y in target_coords:
            perform_click(x, y, delay)
            logger.info(f"Completed iteration {i+1}/{iterations}")