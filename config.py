import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hold_time": 0.05,
    "randomization": False
}

def load_autoclicker_config(filepath: str) -> Dict[str, Any]:
    """Loads configuration from a JSON file with fallback to defaults."""
    if not os.path.exists(filepath):
        save_autoclicker_config(filepath, DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            return {**DEFAULT_CONFIG, **json.load(f)}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_autoclicker_config(filepath: str, config: Dict[str, Any]) -> None:
    """Serializes the autoclicker settings to a JSON file."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

def validate_config_values(config: Dict[str, Any]) -> bool:
    """Ensures that settings fall within operational ranges."""
    if config.get("interval", 0) < 0.001:
        return False
    if config.get("button") not in ["left", "right", "middle"]:
        return False
    return True