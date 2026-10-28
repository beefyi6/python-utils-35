import random
import time
from typing import Tuple


def calculate_jittered_coords(
    coords: Tuple[int, int], radius: int = 3
) -> Tuple[int, int]:
    """Add small random offset to click coordinates to emulate human behavior."""
    x, y = coords
    offset_x = random.randint(-radius, radius)
    offset_y = random.randint(-radius, radius)
    return max(0, x + offset_x), max(0, y + offset_y)


def get_random_delay(base_delay: float, variance: float = 0.1) -> float:
    """Calculate a randomized delay interval to prevent rigid timing patterns."""
    min_delay = max(0.001, base_delay - variance)
    max_delay = base_delay + variance
    return random.uniform(min_delay, max_delay)


def format_duration(seconds: float) -> str:
    """Format elapsed execution time in seconds into a readable string."""
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)
    if hrs > 0:
        return f"{hrs}h {mins}m {secs}s"
    if mins > 0:
        return f"{mins}m {secs}s"
    return f"{seconds:.2f}s" if seconds < 1 else f"{secs}s"


def sleep_with_jitter(base_interval: float, jitter_ratio: float = 0.05) -> None:
    """Pause execution for a randomized duration around the base interval."""
    variance = base_interval * jitter_ratio
    actual_delay = get_random_delay(base_interval, variance)
    time.sleep(actual_delay)


def is_within_bounds(coords: Tuple[int, int], screen_size: Tuple[int, int]) -> bool:
    """Check if target coordinates reside within current screen dimensions."""
    x, y = coords
    max_x, max_y = screen_size
    return 0 <= x < max_x and 0 <= y < max_y
