import random
import time
from typing import Tuple


def calculate_jitter_location(
    x: int, y: int, radius: int = 3
) -> Tuple[int, int]:
    """Apply a small random Gaussian offset to coordinates to mimic human movement."""
    jitter_x = int(random.gauss(x, radius / 2))
    jitter_y = int(random.gauss(y, radius / 2))
    return jitter_x, jitter_y


def get_random_delay(base_cps: float, variation: float = 0.2) -> float:
    """Calculate a randomized delay in seconds based on target clicks per second (CPS)."""
    if base_cps <= 0:
        raise ValueError("CPS must be greater than zero")

    target_delay = 1.0 / base_cps
    min_delay = max(0.001, target_delay * (1.0 - variation))
    max_delay = target_delay * (1.0 + variation)

    return random.uniform(min_delay, max_delay)


def is_within_bounds(
    x: int, y: int, screen_width: int, screen_height: int
) -> bool:
    """Check if the given coordinates fall within the specified screen bounds."""
    return 0 <= x < screen_width and 0 <= y < screen_height


def sleep_with_jitter(base_cps: float, variation: float = 0.2) -> None:
    """Block execution for a randomized delay corresponding to the desired CPS."""
    delay = get_random_delay(base_cps, variation)
    time.sleep(delay)
