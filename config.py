import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "interval_ms": 100,
    "button": "left",
    "click_type": "single",
    "hotkey": "f6",
    "repeat_until_stopped": True,
    "max_clicks": 0,
    "random_jitter_ms": 10
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """
    Loads application configuration from a JSON file.
    If the file does not exist, creates it with default settings.
    """
    config = DEFAULT_CONFIG.copy()

    if not os.path.exists(filepath):
        save_config(config, filepath)
        return config

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, OSError):
        return DEFAULT_CONFIG.copy()

    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> bool:
    """Saves the configuration dictionary to a JSON file."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        return True
    except OSError:
        return False
