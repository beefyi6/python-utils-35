import re
from typing import Dict, Any, Optional

def validate_click_config(config: Dict[str, Any]) -> bool:
    """
    Validates the structure and range of autoclicker configuration values.
    Returns True if valid, raises ValueError otherwise.
    """
    required_keys = {'interval', 'button', 'repeat_count'}
    if not all(key in config for key in required_keys):
        raise ValueError(f"Missing required config keys: {required_keys - config.keys()}")

    if not isinstance(config['interval'], (int, float)) or config['interval'] < 0.01:
        raise ValueError("Interval must be a number >= 0.01 seconds.")

    if config['button'] not in ('left', 'right', 'middle'):
        raise ValueError("Button must be one of: left, right, middle.")

    if not isinstance(config['repeat_count'], int) or config['repeat_count'] < -1:
        raise ValueError("Repeat count must be -1 (infinite) or positive integer.")

    return True

def sanitize_hotkey_string(hotkey: str) -> str:
    """
    Ensures hotkey input conforms to expected format for input simulation.
    """
    clean_key = re.sub(r'[^a-zA-Z0-9+]', '', hotkey).lower()
    if not clean_key:
        raise ValueError("Invalid hotkey characters provided.")
    return clean_key