import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "cps": 10.0,
    "button": "left",
    "hotkey": "f6",
    "click_type": "single",
    "random_jitter": 0.05,
    "max_clicks": 0,
    "target_location": None,
}


class ConfigManager:
    """Manages loading, merging, and saving autoclicker settings."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.settings: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from disk, falling back to defaults for missing keys."""
        if self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    loaded_data = json.load(f)
                    if isinstance(loaded_data, dict):
                        self.settings.update(loaded_data)
            except (json.JSONDecodeError, OSError):
                pass
        return self.settings

    def save(self) -> bool:
        """Saves current configuration to JSON file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.settings, f, indent=4)
            return True
        except OSError:
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a specific setting value."""
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Update a specific setting value."""
        self.settings[key] = value
