import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat": True
}

def load_config(filepath="config.json"):
    """Load configuration from JSON or return defaults if missing."""
    if not os.path.exists(filepath):
        _save_defaults(filepath)
        return DEFAULT_CONFIG

    try:
        with open(filepath, "r") as f:
            config = json.load(f)
            # Merge with defaults to ensure missing keys are present
            return {**DEFAULT_CONFIG, **config}
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def _save_defaults(filepath):
    """Initialize config file with default values."""
    try:
        with open(filepath, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
    except IOError as e:
        print(f"Could not initialize config: {e}")

if __name__ == "__main__":
    # Example usage for verification
    app_config = load_config()
    print(f"Active config: {app_config}")