import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "click_button": "left",
    "repeat_times": 10,
    "hotkey": "f8"
}

def load_config(filepath: str) -> dict:
    """
    Loads configuration from a JSON file, merging with defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        return config

    try:
        with open(filepath, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass

    return config

def save_config(filepath: str, config: dict) -> None:
    """
    Persists the current configuration to a JSON file.
    """
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)