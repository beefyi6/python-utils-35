import random
import time
from typing import Tuple


def calculate_jitter(
    coords: Tuple[int, int], max_jitter: int = 3
) -> Tuple[int, int]:
    """Applies a small random offset to target coordinates to mimic human clicking."""
    x, y = coords
    jitter_x = random.randint(-max_jitter, max_jitter)
    jitter_y = random.randint(-max_jitter, max_jitter)
    return x + jitter_x, y + jitter_y


def sleep_with_variation(base_delay: float, variation: float = 0.1) -> None:
    """Suspends execution for a base delay plus or minus a random variation."""
    if base_delay <= 0:
        return
    min_delay = max(0.001, base_delay - variation)
    max_delay = base_delay + variation
    actual_delay = random.uniform(min_delay, max_delay)
    time.sleep(actual_delay)


class ClickRateLimiter:
    """Utility to throttle clicking operations to a maximum clicks-per-second (CPS)."""

    def __init__(self, max_cps: float):
        self.interval = 1.0 / max_cps if max_cps > 0 else 0.0
        self.last_click_time = 0.0

    def wait_if_needed(self) -> None:
        """Blocks progress if the click rate limit would be exceeded."""
        current_time = time.perf_counter()
        elapsed = current_time - self.last_click_time
        if elapsed < self.interval:
            time.sleep(self.interval - elapsed)
        self.last_click_time = time.perf_counter()
