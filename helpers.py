import time
import random
from typing import Tuple

def get_random_delay(min_ms: int, max_ms: int) -> float:
    """
    Calculate a random delay in seconds between two millisecond bounds.

    Args:
        min_ms: Minimum delay in milliseconds.
        max_ms: Maximum delay in milliseconds.

    Returns:
        Randomized delay duration in seconds.
    """
    return random.uniform(min_ms, max_ms) / 1000.0

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """
    Verify if coordinate is within the current display boundaries.

    Args:
        x: Horizontal coordinate.
        y: Vertical coordinate.
        screen_width: Maximum horizontal limit.
        screen_height: Maximum vertical limit.

    Returns:
        True if coordinate is valid, False otherwise.
    """
    return 0 <= x < screen_width and 0 <= y < screen_height

def format_click_summary(count: int, duration: float) -> str:
    """
    Generate a formatted string summary for the user interface.

    Args:
        count: Number of clicks performed.
        duration: Total execution time in seconds.

    Returns:
        Human-readable summary string.
    """
    avg_speed: float = duration / count if count > 0 else 0
    return f"performed {count} clicks at {avg_speed:.4f}s interval average"