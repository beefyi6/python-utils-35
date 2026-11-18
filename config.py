import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "hold_time": 0.05,
    "auto_start": False
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Loads configuration from JSON file or returns defaults."""
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

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists configuration dictionary to JSON file."""
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)