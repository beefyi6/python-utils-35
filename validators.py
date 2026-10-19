"""Validation utilities for autoclicker configuration and input parameters."""

from typing import Tuple, Union


def validate_click_interval(interval: Union[int, float]) -> float:
    """Validate and normalize the time interval between consecutive clicks.

    Args:
        interval: Duration in seconds between clicks.

    Returns:
        The interval as a floating-point number.

    Raises:
        ValueError: If the interval is negative or zero.
    """
    parsed_interval = float(interval)
    if parsed_interval <= 0:
        raise ValueError("Click interval must be a positive number.")
    return parsed_interval


def validate_click_position(
    x: int, y: int, max_x: int, max_y: int
) -> Tuple[int, int]:
    """Ensure screen coordinates are within valid monitor bounds.

    Args:
        x: Target horizontal coordinate.
        y: Target vertical coordinate.
        max_x: Maximum screen width boundary.
        max_y: Maximum screen height boundary.

    Returns:
        A tuple of validated (x, y) coordinates.

    Raises:
        ValueError: If coordinates fall outside screen dimensions.
    """
    if not (0 <= x <= max_x and 0 <= y <= max_y):
        raise ValueError(
            f"Coordinates ({x}, {y}) are out of bounds (0-{max_x}, 0-{max_y})."
        )
    return x, y


def validate_button(button: str) -> str:
    """Validate mouse button selection.

    Args:
        button: The mouse button name ('left', 'right', 'middle').

    Returns:
        Lowercase string representation of the validated button.

    Raises:
        ValueError: If the button name is not recognized.
    """
    valid_buttons = {"left", "right", "middle"}
    normalized = button.strip().lower()
    if normalized not in valid_buttons:
        raise ValueError(f"Invalid button '{button}'. Allowed: {valid_buttons}")
    return normalized
