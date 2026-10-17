import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_count": -1
}

def load_config(filepath: str = "config.json") -> dict:
    """Loads configuration from file or returns defaults."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG.copy()

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            # Merge user config with defaults
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            return config
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG.copy()

def save_config(config: dict, filepath: str = "config.json") -> None:
    """Persists current configuration to file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)