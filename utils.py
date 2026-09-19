import time
import logging
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

def validate_click_interval(interval: float) -> float:
    """Validate and sanitize click interval in seconds."""
    try:
        val = float(interval)
        if val < 0.001:
            logger.warning("Interval %s too small, clamping to 0.001s", interval)
            return 0.001
        if val > 3600.0:
            logger.warning("Interval %s exceeds 1 hour limit, clamping to 3600s", interval)
            return 3600.0
        return val
    except (ValueError, TypeError) as err:
        logger.error("Invalid interval type or value: %s (%s)", interval, err)
        raise ValueError(f"Click interval must be a valid number: {interval}") from err


def clamp_coordinates(x: int, y: int, screen_bounds: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Ensure target click coordinates stay within specified screen bounds."""
    min_x, min_y, max_x, max_y = screen_bounds
    
    if min_x > max_x or min_y > max_y:
        raise ValueError(f"Invalid screen bounds geometry: {screen_bounds}")
        
    clamped_x = max(min_x, min(int(x), max_x))
    clamped_y = max(min_y, min(int(y), max_y))
    
    if (clamped_x, clamped_y) != (x, y):
        logger.debug("Coordinates (%s, %s) clamped to (%s, %s)", x, y, clamped_x, clamped_y)
        
    return clamped_x, clamped_y


def safe_delay(seconds: float) -> bool:
    """Perform a sleep delay with error handling for unexpected values."""
    try:
        delay = validate_click_interval(seconds)
        time.sleep(delay)
        return True
    except Exception as err:
        logger.error("Failed to execute safe delay: %s", err)
        return False
