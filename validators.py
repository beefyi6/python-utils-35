"""Validation utilities for autoclicker inputs and screen boundaries."""

from typing import Tuple, Optional


class ValidationError(Exception):
    """Custom exception raised when autoclicker configuration validation fails."""
    pass


def validate_interval(cps: Optional[float] = None, interval: Optional[float] = None) -> float:
    """Validate and calculate the delay interval between clicks in seconds."""
    if cps is not None and interval is not None:
        raise ValidationError("Provide either 'cps' or 'interval', not both")

    if cps is not None:
        if not isinstance(cps, (int, float)) or cps <= 0:
            raise ValidationError(f"CPS must be a positive number, got: {cps}")
        if cps > 1000:
            raise ValidationError(f"CPS exceeds maximum safe threshold (1000), got: {cps}")
        return 1.0 / cps

    if interval is not None:
        if not isinstance(interval, (int, float)) or interval < 0:
            raise ValidationError(f"Interval must be a non-negative number, got: {interval}")
        return float(interval)

    # Default fallback interval (0.1 seconds / 10 CPS)
    return 0.1


def validate_coordinates(
    coords: Optional[Tuple[int, int]],
    screen_size: Optional[Tuple[int, int]] = None
) -> Optional[Tuple[int, int]]:
    """Ensure click coordinates are valid non-negative integers within screen bounds."""
    if coords is None:
        return None

    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise ValidationError(f"Coordinates must be a tuple of (x, y), got: {coords}")

    x, y = coords
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValidationError(f"Coordinate values must be integers, got: ({type(x)}, {type(y)})")

    if x < 0 or y < 0:
        raise ValidationError(f"Coordinates cannot be negative: ({x}, {y})")

    if screen_size is not None:
        max_x, max_y = screen_size
        if x >= max_x or y >= max_y:
            raise ValidationError(f"Target point ({x}, {y}) is outside screen bounds ({max_x}x{max_y})")

    return int(x), int(y)


def validate_click_count(count: int) -> int:
    """Validate click count parameter, where 0 represents infinite clicks."""
    if not isinstance(count, int):
        raise ValidationError(f"Click count must be an integer, got: {type(count).__name__}")
    if count < 0:
        raise ValidationError(f"Click count cannot be negative, got: {count}")
    return count
