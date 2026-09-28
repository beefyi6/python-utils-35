import sys
from typing import Tuple, Union, Optional

class ValidationError(ValueError):
    """Exception raised for validation errors in the autoclicker configuration."""
    pass

def validate_interval(interval: Union[int, float]) -> float:
    """Validates the click interval in seconds."""
    try:
        val = float(interval)
    except (TypeError, ValueError):
        raise ValidationError(f"Interval must be a number, got {interval}")
    
    if val < 0.001:
        raise ValidationError("Interval must be at least 0.001 seconds.")
    return val

def validate_button(button: str) -> str:
    """Validates that the button is a recognized mouse button."""
    allowed = {"left", "right", "middle"}
    clean_button = str(button).strip().lower()
    if clean_button not in allowed:
        raise ValidationError(f"Button must be one of {allowed}, got '{button}'")
    return clean_button

def validate_clicks(clicks: int) -> int:
    """Validates the number of clicks, where 0 represents infinite clicks."""
    try:
        val = int(clicks)
    except (TypeError, ValueError):
        raise ValidationError(f"Clicks count must be an integer, got {clicks}")
    
    if val < 0:
        raise ValidationError("Clicks count must be 0 (for infinite) or greater.")
    return val

def validate_coordinates(coords: Optional[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
    """Validates screen coordinates if they are provided."""
    if coords is None:
        return None
    
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        raise ValidationError("Coordinates must be a tuple or list of (x, y) or None.")
    
    try:
        x, y = int(coords[0]), int(coords[1])
    except (TypeError, ValueError):
        raise ValidationError(f"Coordinates must contain valid integers, got {coords}")
        
    if x < 0 or y < 0:
        raise ValidationError(f"Coordinates cannot be negative, got ({x}, {y})")
        
    return (x, y)