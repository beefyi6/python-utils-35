import math
import random
from typing import Optional, Tuple


class AutoclickerError(Exception):
    """Base exception for autoclicker helper operations."""
    pass


class InvalidCoordinateError(AutoclickerError):
    """Raised when target coordinates are out of bounds or invalid."""
    pass


class InvalidIntervalError(AutoclickerError):
    """Raised when click interval is non-positive or unfeasible."""
    pass


def validate_click_interval(interval: float, min_interval: float = 0.001) -> float:
    """Validate and normalize click interval in seconds.
    
    Handles edge cases like negative values, zero, or non-numeric types.
    """
    if not isinstance(interval, (int, float)):
        raise InvalidIntervalError(f"Interval must be a number, got {type(interval).__name__}")
    
    if math.isnan(interval) or math.isinf(interval):
        raise InvalidIntervalError("Interval cannot be NaN or infinite")
        
    if interval < min_interval:
        raise InvalidIntervalError(
            f"Interval {interval}s is below minimum safe threshold ({min_interval}s)"
        )
        
    return float(interval)


def safe_parse_coordinates(
    coords: Tuple[object, object], 
    screen_bounds: Optional[Tuple[int, int]] = None
) -> Tuple[int, int]:
    """Parse and validate screen coordinates with boundary checks.
    
    Handles float truncation, string conversion, and out-of-bounds edge cases.
    """
    try:
        x = int(coords[0])
        y = int(coords[1])
    except (ValueError, TypeError, IndexError) as err:
        raise InvalidCoordinateError(f"Failed to parse coordinates from {coords}: {err}")

    if x < 0 or y < 0:
        raise InvalidCoordinateError(f"Coordinates cannot be negative: ({x}, {y})")

    if screen_bounds:
        max_x, max_y = screen_bounds
        if x > max_x or y > max_y:
            raise InvalidCoordinateError(
                f"Coordinates ({x}, {y}) exceed screen bounds ({max_x}, {max_y})"
            )

    return x, y


def calculate_jitter(x: int, y: int, max_offset: int = 2) -> Tuple[int, int]:
    """Apply subtle coordinate offset while ensuring non-negative target position."""
    safe_offset = min(abs(max_offset), 10)
    offset_x = random.randint(-safe_offset, safe_offset)
    offset_y = random.randint(-safe_offset, safe_offset)
    
    return max(0, x + offset_x), max(0, y + offset_y)
