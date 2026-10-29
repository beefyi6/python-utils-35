import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "clicks_per_second": 10.0,
    "mouse_button": "left",
    "toggle_hotkey": "f6",
    "randomize_interval": True,
    "jitter_range_ms": 15,
    "click_type": "single",
    "max_clicks": 0,
}

class ConfigLoader:
    """Handles loading and validation of autoclicker configuration settings."""

    def __init__(self, config_filepath: str = "config.json"):
        self.filepath = Path(config_filepath)
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load configuration from disk, applying defaults for missing values."""
        if not self.filepath.exists():
            self.save(self.config)
            return self.config

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)

            for key, val in user_config.items():
                if key in DEFAULT_CONFIG:
                    self.config[key] = val
        except (json.JSONDecodeError, OSError):
            self.config = DEFAULT_CONFIG.copy()

        return self.config

    def save(self, data: Dict[str, Any]) -> bool:
        """Save current configuration dictionary to file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True
        except OSError:
            return False
