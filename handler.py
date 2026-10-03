import logging
from pynput.mouse import Controller

logger = logging.getLogger(__name__)
mouse = Controller()

def safe_click(x: int, y: int) -> bool:
    """Performs a mouse click with boundary and system checks."""
    try:
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError(f"Coordinates must be integers, got ({type(x)}, {type(y)})")
        
        if x < 0 or y < 0:
            logger.error(f"Invalid negative coordinates: ({x}, {y})")
            return False
            
        mouse.position = (x, y)
        mouse.click(0, 1)
        return True
        
    except PermissionError:
        logger.error("Insufficient system permissions for mouse control")
    except Exception as e:
        logger.critical(f"Unexpected automation failure: {e}")
    
    return False

def validate_interval(seconds: float) -> float:
    """Ensures click interval is within safe operating range."""
    min_safe = 0.01
    if seconds < min_safe:
        logger.warning(f"Interval {seconds}s below threshold, capping at {min_safe}s")
        return min_safe
    return float(seconds)