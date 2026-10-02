import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "delay_seconds": 0.1,
    "mouse_button": "left",  # options: left, right, middle
    "click_type": "single",   # options: single, double
    "hotkey": "f8",
    "random_delay_range": [0.0, 0.05],
    "hold_time_seconds": 0.01
}

class ConfigLoader:
    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = Path(config_path)
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from a file, falling back to defaults for missing options."""
        if not self.config_path.exists():
            self.save_defaults()
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_data = json.load(f)
            
            # Merge loaded configurations with the defaults
            merged = DEFAULT_CONFIG.copy()
            for key, val in user_data.items():
                if key in merged and isinstance(val, type(merged[key])):
                    merged[key] = val
            return merged
        except (json.JSONDecodeError, OSError):
            # Return default config if file is corrupted or unreadable
            return DEFAULT_CONFIG.copy()

    def save_defaults(self) -> None:
        """Saves standard default settings to configuration file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
        except OSError:
            pass

    def get(self, key: str) -> Any:
        """Access config options with safety fallback."""
        return self.config.get(key, DEFAULT_CONFIG.get(key))
