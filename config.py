import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "cps": 10.0,
    "button": "left",
    "hotkey": "f6",
    "random_interval_ms": 15,
    "click_limit": 0,
    "double_click": False,
}


class ConfigLoader:
    """Handles loading, validating, and saving autoclicker configurations."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load configuration from disk, applying default values for missing keys."""
        if not os.path.exists(self.config_path):
            self.save()
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_data = json.load(f)
                if isinstance(user_data, dict):
                    for key, value in user_data.items():
                        if key in DEFAULT_CONFIG:
                            self.config[key] = value
        except (json.JSONDecodeError, OSError):
            self.config = DEFAULT_CONFIG.copy()

        return self.config

    def save(self) -> None:
        """Save current configuration to disk."""
        target_dir = os.path.dirname(self.config_path)
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)

    def get(self, key: str) -> Any:
        """Retrieve a configuration option."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))
