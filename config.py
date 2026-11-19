import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "hotkey": "f6"
}

def load_configuration(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from json file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        save_configuration(filepath, config)
        return config

    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_configuration(filepath: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to a json file."""
    try:
        with open(filepath, "w") as f:
            json.dump(config, f, indent=4)
    except IOError:
        pass