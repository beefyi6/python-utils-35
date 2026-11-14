import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "clicks_per_second": 10.0,
    "mouse_button": "left",
    "click_type": "single",
    "hotkey": "f6",
    "random_jitter": 0.02,
    "max_clicks": 0,
}


class ConfigManager:
    """Handles loading, updating, and persisting autoclicker settings."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from file, merging with default values."""
        if not os.path.exists(self.config_path):
            self.save()
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                user_config = json.load(file)
                if isinstance(user_config, dict):
                    for key, default_value in DEFAULT_CONFIG.items():
                        self.config[key] = user_config.get(key, default_value)
        except (json.JSONDecodeError, OSError):
            self.config = DEFAULT_CONFIG.copy()

        return self.config

    def save(self) -> bool:
        """Saves the current configuration to a JSON file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as file:
                json.dump(self.config, file, indent=4)
            return True
        except OSError:
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a single configuration parameter value."""
        return self.config.get(key, default)
