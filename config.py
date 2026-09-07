import os
import json
import logging

# Default configuration settings
DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "repeat": True
}

def load_config(filepath: str) -> dict:
    """Loads and validates the configuration file."""
    if not os.path.exists(filepath):
        logging.warning("Config file not found, creating default.")
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Validate mandatory fields
            if not isinstance(data.get("click_interval"), (int, float)):
                raise ValueError("Invalid click_interval type")
            return data
    except (json.JSONDecodeError, ValueError, PermissionError) as e:
        logging.error(f"Failed to load config: {e}. Falling back.")
        return DEFAULT_CONFIG

def save_config(filepath: str, data: dict) -> bool:
    """Safely writes the configuration to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        return True
    except (IOError, TypeError) as e:
        logging.error(f"Could not write config file: {e}")
        return False