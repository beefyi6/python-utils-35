import json
import os
from typing import Dict, Any, Optional

DEFAULT_CONFIG_PATH = "config.json"

def load_clicker_settings(filepath: str = DEFAULT_CONFIG_PATH) -> Dict[str, Any]:
    """Loads autoclicker parameters from a local JSON file."""
    if not os.path.exists(filepath):
        return {"interval": 0.1, "button": "left", "repeat": -1}
    
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

def save_clicker_settings(data: Dict[str, Any], filepath: str = DEFAULT_CONFIG_PATH) -> bool:
    """Persists current clicker configuration to storage."""
    try:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except IOError:
        return False

def validate_interval(interval: Any) -> float:
    """Ensures click interval is a safe positive number."""
    try:
        val = float(interval)
        return max(0.01, val)
    except (ValueError, TypeError):
        return 0.1

def format_coords(x: int, y: int) -> str:
    """Utility for logging coordinate points accurately."""
    return f"({int(x)}, {int(y)})"