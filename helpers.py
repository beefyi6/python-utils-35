import random
import time
from typing import Tuple


def calculate_jitter_delay(base_interval: float, jitter_percentage: float = 0.1) -> float:
    """Calculate a randomized delay interval to simulate human clicking variance."""
    if base_interval <= 0:
        return 0.0
    
    variance = base_interval * max(0.0, min(1.0, jitter_percentage))
    delay = random.uniform(base_interval - variance, base_interval + variance)
    return max(0.001, delay)


def parse_interval(value: str) -> float:
    """Parse human-readable interval strings like '500ms', '1.5s', or '2m' into seconds."""
    val = value.strip().lower()
    if val.endswith("ms"):
        return float(val[:-2]) / 1000.0
    elif val.endswith("s"):
        return float(val[:-1])
    elif val.endswith("m"):
        return float(val[:-1]) * 60.0
    
    return float(val)


def clamp_coordinates(x: int, y: int, screen_bounds: Tuple[int, int, int, int]) -> Tuple[int, int]:
    """Ensure screen coordinates stay within specified screen boundaries (min_x, min_y, max_x, max_y)."""
    min_x, min_y, max_x, max_y = screen_bounds
    clamped_x = max(min_x, min(x, max_x))
    clamped_y = max(min_y, min(y, max_y))
    return clamped_x, clamped_y


def cps_to_interval(cps: float) -> float:
    """Convert target clicks per second (CPS) into standard delay interval in seconds."""
    if cps <= 0:
        raise ValueError("CPS target must be greater than zero")
    return 1.0 / cps
