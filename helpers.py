import random
import time
from typing import Tuple


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a numerical value between a minimum and maximum bound."""
    return max(min_val, min(value, max_val))


def cps_to_delay(cps: float) -> float:
    """Convert clicks per second (CPS) to interval delay in seconds."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def delay_to_cps(delay: float) -> float:
    """Convert interval delay in seconds to clicks per second (CPS)."""
    if delay <= 0:
        raise ValueError("Delay must be greater than zero.")
    return 1.0 / delay


def calculate_jitter_delay(base_delay: float, jitter_percentage: float = 0.1) -> float:
    """
    Calculate a randomized delay interval to simulate human variation.

    :param base_delay: Target delay between clicks in seconds.
    :param jitter_percentage: Maximum variance percentage (0.0 to 1.0).
    :return: Randomized delay in seconds.
    """
    jitter_percentage = clamp(jitter_percentage, 0.0, 1.0)
    max_variance = base_delay * jitter_percentage
    variance = random.uniform(-max_variance, max_variance)
    return max(0.001, base_delay + variance)


def format_coordinates(x: int, y: int) -> str:
    """Format screen coordinates into standard readable format."""
    return f"({x}, {y})"


def precise_sleep(seconds: float) -> None:
    """High precision sleep suitable for fast auto-clicking loops."""
    target_time = time.perf_counter() + seconds
    while time.perf_counter() < target_time:
        remaining = target_time - time.perf_counter()
        if remaining > 0.002:
            time.sleep(remaining - 0.001)
