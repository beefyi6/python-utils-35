import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "click_delay": 0.1,
    "mouse_button": "left",
    "start_hotkey": "f1",
    "stop_hotkey": "f2",
    "max_clicks": 0,
    "random_delay_range": [0.0, 0.0]
}

class ConfigLoader:
    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self.config = self.load()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from JSON file, creating it with defaults if missing."""
        if not os.path.exists(self.filepath):
            self._save_defaults()
            return DEFAULT_CONFIG.copy()
        
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
            # Merge user config with defaults to ensure all keys exist
            loaded_config = DEFAULT_CONFIG.copy()
            loaded_config.update(user_config)
            return loaded_config
        except (json.JSONDecodeError, OSError):
            # Fallback to defaults in case of corrupt file
            return DEFAULT_CONFIG.copy()

    def _save_defaults(self) -> None:
        """Saves default configuration to the file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except OSError:
            pass

    def get(self, key: str) -> Any:
        """Gets a configuration value, returning default if missing."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def update(self, key: str, value: Any) -> None:
        """Updates a specific configuration option and saves it."""
        self.config[key] = value
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
        except OSError:
            pass