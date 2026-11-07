"""Validation utilities for autoclicker configuration and parameters."""

import math
from typing import Tuple, Union


def validate_click_interval(interval: Union[int, float]) -> float:
    """Validate click interval in seconds.

    Handles non-numeric types, NaN, infinite values, and extreme bounds.
    """
    if isinstance(interval, bool):
        raise TypeError(f"Interval cannot be a boolean value: {interval}")

    try:
        val = float(interval)
    except (ValueError, TypeError) as err:
        raise ValueError(f"Invalid click interval value: {interval}") from err

    if math.isnan(val) or math.isinf(val):
        raise ValueError("Click interval must be a finite real number")

    if val < 0.001:
        raise ValueError("Click interval must be at least 0.001 seconds (1ms)")

    if val > 86400.0:
        raise ValueError("Click interval exceeds maximum limit of 86400 seconds")

    return round(val, 6)


def validate_coordinates(x: int, y: int, max_x: int = 7680, max_y: int = 4320) -> Tuple[int, int]:
    """Validate screen coordinates against acceptable display boundaries."""
    for name, coord in [("x", x), ("y", y)]:
        if isinstance(coord, bool) or not isinstance(coord, int):
            raise TypeError(f"Coordinate {name} must be an integer")

    if x < 0 or x > max_x:
        raise ValueError(f"X coordinate {x} is outside allowed range [0, {max_x}]")

    if y < 0 or y > max_y:
        raise ValueError(f"Y coordinate {y} is outside allowed range [0, {max_y}]")

    return x, y


def validate_mouse_button(button: str) -> str:
    """Validate mouse button target string."""
    if not isinstance(button, str):
        raise TypeError(f"Mouse button must be a string, got {type(button).__name__}")

    cleaned = button.strip().lower()
    valid_buttons = {"left", "right", "middle"}

    if cleaned not in valid_buttons:
        raise ValueError(f"Invalid mouse button '{button}'. Allowed: {sorted(valid_buttons)}")

    return cleaned
