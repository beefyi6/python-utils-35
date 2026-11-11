import typing

def validate_click_params(interval: float, count: int) -> bool:
    """
    Ensures click parameters are within safe hardware limits.
    Returns True if valid, raises ValueError otherwise.
    """
    if not isinstance(interval, (int, float)):
        raise ValueError("Interval must be a numeric value.")
    
    if interval < 0.001:
        raise ValueError("Interval below 1ms can cause system instability.")
        
    if not isinstance(count, int):
        raise ValueError("Click count must be an integer.")
        
    if count < -1:
        raise ValueError("Count must be -1 for infinite or > 0 for finite.")
        
    return True

def sanitize_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> typing.Tuple[int, int]:
    """
    Clamps mouse coordinates to current screen boundaries.
    """
    clamped_x = max(0, min(x, screen_width))
    clamped_y = max(0, min(y, screen_height))
    return (clamped_x, clamped_y)