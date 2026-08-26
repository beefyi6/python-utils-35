import json
import os

DEFAULT_CONFIG = {
    "cps": 10,
    "hotkey": "f6",
    "hold_time": 0.01,
    "toggle_mode": True
}

class ConfigLoader:
    def __init__(self, filepath="config.json"):
        self.filepath = filepath
        self.settings = DEFAULT_CONFIG.copy()
        self.load()

    def load(self):
        """Load configuration from file or fallback to defaults."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    user_data = json.load(f)
                    self.settings.update(user_data)
            except (json.JSONDecodeError, IOError):
                pass
        else:
            self.save()

    def save(self):
        """Save current configuration to file."""
        try:
            with open(self.filepath, "w") as f:
                json.dump(self.settings, f, indent=4)
        except IOError:
            pass

    def get(self, key):
        """Retrieve a configuration value safely."""
        return self.settings.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        """Update and persist a configuration value."""
        self.settings[key] = value
        self.save()
