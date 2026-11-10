import time
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

def format_coordinates(x: int, y: int) -> Tuple[int, int]:
    """Validate and sanitize screen coordinates."""
    return max(0, x), max(0, y)

def get_wait_interval(base_interval: float, jitter: float) -> float:
    """Calculate randomized delay to simulate human behavior."""
    import random
    variation = random.uniform(-jitter, jitter)
    return max(0.1, base_interval + variation)

def log_click_event(x: int, y: int, action: str = "click") -> None:
    """Standardized logging format for click events."""
    logger.info(f"Action: {action} at coordinates ({x}, {y})")

def validate_timeout(seconds: float) -> float:
    """Ensure timeout is within acceptable operational bounds."""
    if seconds < 0:
        logger.warning("Negative timeout detected, defaulting to 0")
        return 0.0
    return float(seconds)

def safe_sleep(seconds: float) -> None:
    """Execute sleep with float precision validation."""
    time.sleep(validate_timeout(seconds))