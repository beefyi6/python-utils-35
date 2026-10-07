import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": True
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    if not os.path.exists(filepath):
        save_config(DEFAULT_CONFIG, filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists configuration to disk."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)