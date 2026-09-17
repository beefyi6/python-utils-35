import os
import json
import logging

# Default configuration for autoclicker
DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "max_clicks": 1000
}

def load_config(filepath):
    """Load configuration with strict error validation."""
    if not os.path.exists(filepath):
        logging.warning("Config file not found, creating default.")
        return DEFAULT_CONFIG

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Validate structure
            if not isinstance(data, dict):
                raise ValueError("Invalid config format")
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, PermissionError, ValueError) as e:
        logging.error(f"Failed to load config: {e}. Using defaults.")
        return DEFAULT_CONFIG

def save_config(filepath, config_data):
    """Save configuration to file with error handling."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config_data, f, indent=4)
    except (IOError, TypeError) as e:
        logging.error(f"Critical error saving configuration: {e}")
        raise RuntimeError("Configuration persistence failed") from e
