import re

def validate_interval(value):
    """Checks if interval is a positive float or int."""
    try:
        val = float(value)
        return val > 0
    except (ValueError, TypeError):
        return False

def validate_coordinates(x, y):
    """Verifies coordinates are non-negative integers."""
    return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0

def validate_hotkey(key):
    """Ensures hotkey string matches standard key naming."""
    pattern = r'^[a-z0-9_]{1,15}$'
    return bool(re.match(pattern, str(key).lower()))

def validate_iterations(count):
    """Validates click iteration count; -1 signifies infinite."""
    try:
        val = int(count)
        return val >= -1
    except (ValueError, TypeError):
        return False