import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "clicks_per_second": 10.0,
    "click_type": "left",
    "hotkey": "f8",
    "hold_to_click": False,
}

class ConfigManager:
    """Manages loading, saving, and updating autoclicker configuration settings."""

    def __init__(self, filepath: str = "autoclicker_config.json") -> None:
        self.filepath = filepath
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads config from disk, falling back to defaults if missing or corrupted."""
        if not os.path.exists(self.filepath):
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Ensure all default keys exist
                for key, val in DEFAULT_CONFIG.items():
                    if key not in data:
                        data[key] = val
                return data
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG.copy()

    def save_config(self, data: Dict[str, Any]) -> None:
        """Saves configuration data safely to a JSON file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            self.config = data
        except IOError:
            pass

    def get(self, key: str) -> Any:
        """Retrieves a setting value, falling back to default if not found."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def update_setting(self, key: str, value: Any) -> None:
        """Updates a single configuration setting and persists the change."""
        if key in DEFAULT_CONFIG:
            self.config[key] = value
            self.save_config(self.config)