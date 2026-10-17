import logging

# Configuration constraints for the autoclicker
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0
ALLOWED_BUTTONS = ['left', 'right', 'middle']

def validate_click_params(interval, button):
    """Ensures click settings are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or not (MIN_INTERVAL <= interval <= MAX_INTERVAL):
        logging.error(f"Invalid interval: {interval}. Must be between {MIN_INTERVAL} and {MAX_INTERVAL}.")
        return False

    if button not in ALLOWED_BUTTONS:
        logging.error(f"Invalid button: {button}. Must be one of {ALLOWED_BUTTONS}.")
        return False

    return True

def validate_coordinates(x, y):
    """Checks if screen coordinates are non-negative integers."""
    if not (isinstance(x, int) and isinstance(y, int)):
        return False
    if x < 0 or y < 0:
        return False
    return True

def sanitize_input(user_input):
    """Basic input cleanup for UI parameters."""
    if isinstance(user_input, str):
        return user_input.strip().lower()
    return user_input