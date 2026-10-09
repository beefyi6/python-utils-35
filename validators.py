from typing import Tuple, Union, Optional

class ValidationError(ValueError):
    """Raised when autoclicker configuration parameters are invalid."""
    pass

def validate_click_interval(interval: float) -> float:
    """Validates that the click interval is a positive float."""
    if not isinstance(interval, (int, float)):
        raise ValidationError(f"Interval must be a number, got {type(interval).__name__}")
    if interval <= 0:
        raise ValidationError(f"Interval must be greater than zero, got {interval}")
    return float(interval)

def validate_coordinates(coords: Optional[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
    """Ensures mouse coordinates are valid screen coordinates or None."""
    if coords is None:
        return None
    if not isinstance(coords, tuple) or len(coords) != 2:
        raise ValidationError(f"Coordinates must be a tuple of (x, y), got {coords}")
    x, y = coords
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValidationError("Coordinates must consist of integers only")
    if x < 0 or y < 0:
        raise ValidationError(f"Coordinates cannot be negative, got ({x}, {y})")
    return (x, y)

def validate_click_count(count: int) -> int:
    """Validates click repetition count where 0 indicates infinite looping."""
    if not isinstance(count, int):
        raise ValidationError(f"Click count must be an integer, got {type(count).__name__}")
    if count < 0:
        raise ValidationError(f"Click count cannot be negative, got {count}")
    return count

def validate_button(button: str) -> str:
    """Normalizes and validates target mouse button values."""
    allowed_buttons = {"left", "right", "middle"}
    if not isinstance(button, str):
        raise ValidationError("Mouse button identifier must be a string")
    normalized = button.lower().strip()
    if normalized not in allowed_buttons:
        raise ValidationError(f"Unsupported mouse button '{button}', use: {', '.join(allowed_buttons)}")
    return normalized