import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "toggle_key": "f6"
}

def load_config(filepath: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from disk or returns defaults if missing."""
    config = DEFAULT_CONFIG.copy()
    
    if not os.path.exists(filepath):
        return config
    
    try:
        with open(filepath, "r") as f:
            user_config = json.load(f)
            config.update(user_config)
    except (json.JSONDecodeError, IOError):
        pass
        
    return config

def save_config(config: Dict[str, Any], filepath: str = "config.json") -> None:
    """Persists current configuration state to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=4)