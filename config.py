import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "interval": 0.1,
    "button": "left",
    "repeat": 0,
    "jitter": 0.0
}

def load_config(filepath: str) -> Dict[str, Any]:
    """Loads autoclicker configuration from a JSON file."""
    if not os.path.exists(filepath):
        return DEFAULT_CONFIG
    
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            return {**DEFAULT_CONFIG, **data}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(filepath: str, config: Dict[str, Any]) -> None:
    """Persists current autoclicker settings to disk."""
    try:
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Failed to save configuration: {e}")

def validate_interval(interval: float) -> float:
    """Ensures interval is within safety limits."""
    return max(0.01, min(interval, 60.0))