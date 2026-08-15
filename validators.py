import re

def is_valid_click_speed(speed):
    """Check if click speed is within allowable range."""
    return isinstance(speed, (int, float)) and 0 < speed <= 10

def is_valid_click_count(count):
    """Check if click count is a positive integer."""
    return isinstance(count, int) and count > 0

def is_valid_hotkey(hotkey):
    """Validate if the provided hotkey is in the correct format."""
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    return isinstance(hotkey, str) and pattern.match(hotkey)

def validate_settings(settings):
    """Validate the settings for the autoclicker."""
    if not is_valid_click_speed(settings.get('click_speed')):
        raise ValueError('Invalid click speed')
    if not is_valid_click_count(settings.get('click_count')):
        raise ValueError('Invalid click count')
    if not is_valid_hotkey(settings.get('hotkey')):
        raise ValueError('Invalid hotkey')
    return True
