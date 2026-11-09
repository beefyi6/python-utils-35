import re
from typing import Dict, Any, Optional

def validate_click_config(config: Dict[str, Any]) -> bool:
    """Validates autoclicker configuration parameters."""
    required_fields = ['interval', 'button', 'coordinates']
    
    # Check for presence of mandatory keys
    if not all(key in config for key in required_fields):
        return False

    # Validate interval range (0.01 to 60.0 seconds)
    interval = config.get('interval')
    if not isinstance(interval, (int, float)) or not (0.01 <= interval <= 60.0):
        return False

    # Validate button input
    valid_buttons = ['left', 'right', 'middle']
    if config.get('button') not in valid_buttons:
        return False

    # Validate coordinate format
    coords = config.get('coordinates')
    if not isinstance(coords, tuple) or len(coords) != 2:
        return False
    if not all(isinstance(i, int) and i >= 0 for i in coords):
        return False

    return True

def sanitize_hotkey(key: str) -> Optional[str]:
    """Ensures hotkey string matches alphanumeric format."""
    pattern = re.compile(r'^[a-zA-Z0-9]{1,10}$')
    if pattern.match(key):
        return key.lower()
    return None