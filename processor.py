import json

class DataProcessor:
    def __init__(self, data=None):
        self.data = data or []  # Initialize with an empty list if no data is provided

    def add_data(self, new_data):
        """Add new data to the processor."""
        self.data.append(new_data)

    def remove_data(self, target_data):
        """Remove specific data from the processor if it exists."""
        try:
            self.data.remove(target_data)
        except ValueError:
            print(f'ValueError: {target_data} not found in data')

    def to_json(self):
        """Convert the current data to JSON format."""
        return json.dumps(self.data)

    def from_json(self, json_data):
        """Load data from a JSON string."""
        try:
            self.data = json.loads(json_data)
        except json.JSONDecodeError:
            print('JSONDecodeError: Invalid JSON format')

    def clear_data(self):
        """Clear all stored data."""
        self.data.clear()  

    def get_data(self):
        """Return a copy of the stored data."""
        return self.data.copy()