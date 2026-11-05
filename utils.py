import random
import time
from typing import Tuple


def cps_to_interval(cps: float) -> float:
    """Convert clicks per second (CPS) to seconds per click interval."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def calculate_jittered_delay(base_interval: float, jitter_percentage: float = 0.15) -> float:
    """Add random variation (jitter) to a base delay to mimic human reaction."""
    if base_interval <= 0:
        return 0.0
    
    percentage = max(0.0, min(jitter_percentage, 1.0))
    variation = base_interval * percentage
    jittered = random.uniform(base_interval - variation, base_interval + variation)
    return max(0.001, jittered)


def randomize_point(x: int, y: int, radius: int = 5) -> Tuple[int, int]:
    """Randomize target coordinates within a specified pixel radius."""
    if radius <= 0:
        return x, y
    
    offset_x = int(random.gauss(0, radius / 2.0))
    offset_y = int(random.gauss(0, radius / 2.0))
    
    offset_x = max(-radius, min(radius, offset_x))
    offset_y = max(-radius, min(radius, offset_y))
    
    return x + offset_x, y + offset_y


def parse_delay_range(min_delay: float, max_delay: float) -> float:
    """Return a random delay duration within a min/max bound in seconds."""
    if min_delay > max_delay:
        min_delay, max_delay = max_delay, min_delay
    return random.uniform(max(0.0, min_delay), max(0.0, max_delay))
