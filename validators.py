import re
from typing import Tuple, Any

# Supported mouse buttons for the autoclicker
VALID_BUTTONS = {"left", "right", "middle"}

def validate_coordinates(coords: Any) -> Tuple[int, int]:
    """Validates screen coordinates and returns them as a tuple of integers."""
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise ValueError("Coordinates must be a tuple or list of two integers (x, y).")
    try:
        x, y = int(coords[0]), int(coords[1])
    except (TypeError, ValueError):
        raise ValueError("Coordinate values must be castable to integers.")
    
    if x < 0 or y < 0:
        raise ValueError("Coordinates cannot be negative.")
    return x, y

def validate_interval(interval: Any) -> float:
    """Validates click delay interval in seconds."""
    try:
        val = float(interval)
    except (TypeError, ValueError):
        raise ValueError("Interval must be a valid number.")
    if val < 0.001:
        raise ValueError("Interval must be at least 0.001 seconds (1 millisecond).")
    return val

def validate_click_count(count: Any) -> int:
    """Validates the total number of clicks (0 represents infinite/continuous)."""
    try:
        val = int(count)
    except (TypeError, ValueError):
        raise ValueError("Click count must be a valid integer.")
    if val < 0:
        raise ValueError("Click count cannot be negative (use 0 for infinite).")
    return val

def validate_button(button: str) -> str:
    """Validates that the specified mouse button is supported."""
    if not isinstance(button, str):
        raise TypeError("Button name must be a string.")
    cleaned_button = button.strip().lower()
    if cleaned_button not in VALID_BUTTONS:
        raise ValueError(f"Invalid button '{button}'. Supported: {', '.join(VALID_BUTTONS)}")
    return cleaned_button
