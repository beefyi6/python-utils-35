import json
import os

DEFAULTS = {
    "click_interval": 0.1,
    "click_count": 100,
    "mouse_button": "left",
    "running": false
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULTS.copy()  # Start with defaults
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                try:
                    user_config = json.load(f)
                    self.config.update(user_config)  # Update with user-defined values
                except json.JSONDecodeError:
                    print(f'Error: {self.config_file} is not a valid JSON file.')

    def get(self, key, default=None):
        return self.config.get(key, default)

# Example usage:
# config_loader = ConfigLoader()
# print(config_loader.get('click_interval'))
