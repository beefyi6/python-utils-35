from typing import Tuple, Union


class AutoclickerError(Exception):
    """Base exception for autoclicker utility errors."""
    pass


class InvalidCoordinateError(AutoclickerError):
    """Raised when target coordinates fall outside valid screen bounds."""
    pass


class InvalidIntervalError(AutoclickerError):
    """Raised when the click interval is non-positive or malformed."""
    pass


def validate_screen_bounds(x: int, y: int, max_width: int = 3840, max_height: int = 2160) -> Tuple[int, int]:
    """
    Validates target click coordinates against screen boundaries.

    :param x: Horizontal coordinate
    :param y: Vertical coordinate
    :param max_width: Maximum screen width allowed
    :param max_height: Maximum screen height allowed
    :return: Validated (x, y) tuple
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError(f"Coordinates must be integers, got x={type(x).__name__}, y={type(y).__name__}")

    if x < 0 or y < 0:
        raise InvalidCoordinateError(f"Coordinates cannot be negative: ({x}, {y})")

    if x > max_width or y > max_height:
        raise InvalidCoordinateError(
            f"Target location ({x}, {y}) exceeds screen resolution ({max_width}x{max_height})"
        )

    return x, y


def parse_click_interval(interval: Union[int, float, str]) -> float:
    """
    Ensures click interval is within safe operating bounds.

    :param interval: Desired delay between clicks in seconds
    :return: Normalized delay float
    """
    try:
        val = float(interval)
    except (ValueError, TypeError) as err:
        raise InvalidIntervalError(f"Click interval must be a valid number: {interval}") from err

    if val <= 0.001:
        raise InvalidIntervalError(f"Interval {val}s is too fast or invalid (minimum 0.001s)")

    if val > 86400:
        raise InvalidIntervalError(f"Interval {val}s exceeds maximum allowed duration")

    return round(val, 4)
