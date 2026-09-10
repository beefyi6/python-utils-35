import re

def validate_interval(value):
    """Ensures click interval is a positive float."""
    try:
        f_val = float(value)
        return f_val > 0
    except (ValueError, TypeError):
        return False

def validate_coordinates(x, y):
    """Checks if coordinates are non-negative integers."""
    try:
        return int(x) >= 0 and int(y) >= 0
    except (ValueError, TypeError):
        return False

def validate_hotkey(key):
    """Validates hotkey string format (simple alphanumeric)."""
    if not isinstance(key, str):
        return False
    return bool(re.match(r'^[a-zA-Z0-9+]+$', key))

def sanitize_input(user_input):
    """Strips whitespace and standardizes input for processing."""
    if not isinstance(user_input, str):
        return ""
    return user_input.strip().lower()

def is_positive_integer(value):
    """Verifies that a value is a valid positive integer."""
    try:
        val = int(value)
        return val > 0
    except (ValueError, TypeError):
        return False