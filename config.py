import json
import os

DEFAULT_CONFIG = {
    'click_interval': 0.1,
    'max_clicks': 100,
    'click_button': 'left',
    'run_in_background': False
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
            return {**DEFAULT_CONFIG, **user_config}
        return DEFAULT_CONFIG

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

# Example usage
if __name__ == '__main__':
    config_loader = ConfigLoader()
    print(config_loader.config)  
