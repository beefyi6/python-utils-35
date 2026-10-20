import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "max_clicks": 1000,
    "hotkey": "f6"
}

def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from JSON file with defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            pass
            
    return config

def save_config(config: Dict[str, Any], path: str = "config.json") -> None:
    """Persists current configuration to JSON file."""
    with open(path, "w") as f:
        json.dump(config, f, indent=4)

if __name__ == "__main__":
    current_cfg = load_config()
    print(f"Active configuration: {current_cfg}")