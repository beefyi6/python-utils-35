import random
import time


def calculate_jitter(interval: float, jitter_percent: float = 0.1) -> float:
    """Calculate a randomized interval to simulate human clicking variation.

    :param interval: Base delay between clicks in seconds.
    :param jitter_percent: Maximum percentage variation (0.0 to 1.0).
    :return: Adjusted interval in seconds.
    """
    if interval <= 0:
        return 0.0

    variation = interval * max(0.0, min(jitter_percent, 1.0))
    jittered = interval + random.uniform(-variation, variation)
    return max(0.001, jittered)


def cps_to_interval(cps: float) -> float:
    """Convert clicks per second (CPS) to a time interval in seconds."""
    if cps <= 0:
        raise ValueError("Clicks per second must be greater than zero.")
    return 1.0 / cps


def clamp_cps(cps: float, min_cps: float = 0.1, max_cps: float = 500.0) -> float:
    """Clamp CPS value within acceptable performance boundaries."""
    return max(min_cps, min(cps, max_cps))


def format_elapsed_time(seconds: float) -> str:
    """Format total elapsed seconds into an HH:MM:SS string."""
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def precise_sleep(duration: float) -> None:
    """Perform high-precision sleep for tight autoclicker timing loops."""
    target_time = time.perf_counter() + duration
    while time.perf_counter() < target_time:
        remaining = target_time - time.perf_counter()
        if remaining > 0.002:
            time.sleep(remaining - 0.001)
