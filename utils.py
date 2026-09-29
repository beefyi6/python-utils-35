import time
from typing import Tuple, Callable, Optional


class AutoclickerError(Exception):
    """Base exception for autoclicker utility operations."""
    pass


class OutOfBoundsError(AutoclickerError):
    """Raised when click coordinates fall outside display area."""
    pass


class InvalidIntervalError(AutoclickerError):
    """Raised when click interval is invalid or unsafe."""
    pass


def validate_coordinates(x: int, y: int, screen_bounds: Tuple[int, int]) -> Tuple[int, int]:
    """Validate click coordinates against screen boundaries with safety checks."""
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError(f"Coordinates must be integers, got ({type(x).__name__}, {type(y).__name__})")
    
    max_x, max_y = screen_bounds
    if max_x <= 0 or max_y <= 0:
        raise ValueError(f"Invalid screen dimensions: {screen_bounds}")

    if not (0 <= x < max_x and 0 <= y < max_y):
        raise OutOfBoundsError(f"Target point ({x}, {y}) outside screen area ({max_x}x{max_y})")

    return x, y


def safe_interval_delay(interval_seconds: float, min_limit: float = 0.001) -> float:
    """Ensure click interval is safe and handles negative or near-zero inputs."""
    if not isinstance(interval_seconds, (int, float)):
        raise TypeError("Click interval must be a numerical value")
    
    if interval_seconds < 0:
        raise InvalidIntervalError(f"Interval cannot be negative: {interval_seconds}")

    # Clamp excessively small values to prevent high CPU utilization
    return max(interval_seconds, min_limit)


def execute_safely(action: Callable[..., None], *args, **kwargs) -> bool:
    """Execute click action with exception handling for edge case failures."""
    try:
        action(*args, **kwargs)
        return True
    except AutoclickerError:
        return False
    except (TypeError, ValueError):
        return False
    except Exception as err:
        raise AutoclickerError(f"Unhandled operational failure: {err}") from err
