import time
from typing import Dict, Any, Tuple, Optional

class ValidationError(Exception):
    """Custom exception raised when clicker parameters fail validation."""
    pass

def validate_click_config(config: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    """
    Validates click parameters before starting the main click loop.
    Ensures interval, count, and target coordinates are within safe limits.
    """
    # Validate click interval (in seconds)
    interval = config.get("interval")
    if not isinstance(interval, (int, float)) or interval <= 0.001:
        return False, "Interval must be a positive number >= 0.001 seconds"

    # Validate max click count (0 means infinite)
    max_clicks = config.get("max_clicks", 0)
    if not isinstance(max_clicks, int) or max_clicks < 0:
        return False, "Max clicks must be a non-negative integer"

    # Validate mouse button choice
    button = config.get("button", "left")
    if button not in ("left", "right", "middle"):
        return False, "Button must be 'left', 'right', or 'middle'"

    # Validate target coordinates if provided
    target = config.get("target_coords")
    if target is not None:
        if not isinstance(target, (tuple, list)) or len(target) != 2:
            return False, "Target coordinates must be a tuple of (x, y)"
        x, y = target
        if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
            return False, "Target coordinates (x, y) must be non-negative integers"

    return True, None

def sanitize_loop_input(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitizes and prepares input dictionary for the main execution loop.
    Applies fallback default values for optional parameters.
    """
    valid, error_msg = validate_click_config(raw_data)
    if not valid:
        raise ValidationError(f"Invalid autoclicker settings: {error_msg}")

    return {
        "interval": float(raw_data["interval"]),
        "max_clicks": int(raw_data.get("max_clicks", 0)),
        "button": str(raw_data.get("button", "left")).lower(),
        "target_coords": tuple(raw_data["target_coords"]) if raw_data.get("target_coords") else None,
        "validated_at": time.time()
    }
