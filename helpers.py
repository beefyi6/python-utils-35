from typing import Dict, Any, Tuple, Optional

ALLOWED_BUTTONS = {"left", "right", "middle"}

def validate_click_params(params: Dict[str, Any], screen_bounds: Optional[Tuple[int, int]] = None) -> Dict[str, Any]:
    """
    Validates and cleans input parameters for the main autoclicker execution loop.
    Raises ValueError if any input fails validation criteria.
    """
    validated = {}

    # Validate click interval (seconds between clicks)
    interval = params.get("interval", 0.1)
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError(f"Invalid click interval: {interval}. Must be a positive number.")
    validated["interval"] = float(interval)

    # Validate target mouse button
    button = str(params.get("button", "left")).lower()
    if button not in ALLOWED_BUTTONS:
        raise ValueError(f"Invalid mouse button: '{button}'. Must be one of {ALLOWED_BUTTONS}.")
    validated["button"] = button

    # Validate repetition count (-1 or 0 for infinite, positive int for fixed count)
    repeat = params.get("repeat", 0)
    if not isinstance(repeat, int) or repeat < -1:
        raise ValueError(f"Invalid repeat count: {repeat}. Must be an integer >= -1.")
    validated["repeat"] = repeat

    # Validate target screen coordinates if provided
    coords = params.get("coordinates")
    if coords is not None:
        if not isinstance(coords, (tuple, list)) or len(coords) != 2:
            raise ValueError("Coordinates must be a 2-element tuple or list (x, y).")
        x, y = coords
        if not (isinstance(x, int) and isinstance(y, int)):
            raise ValueError("Coordinate values x and y must be integers.")
        if x < 0 or y < 0:
            raise ValueError(f"Coordinates cannot be negative: ({x}, {y}).")
        if screen_bounds:
            max_x, max_y = screen_bounds
            if x > max_x or y > max_y:
                raise ValueError(f"Coordinates ({x}, {y}) exceed screen bounds ({max_x}, {max_y}).")
        validated["coordinates"] = (x, y)
    else:
        validated["coordinates"] = None

    return validated
