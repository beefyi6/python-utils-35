import json

class InputValidationError(Exception):
    pass

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def validate_input(self):
        if not isinstance(self.data, dict):
            raise InputValidationError('Input must be a dictionary')
        if 'name' not in self.data or not self.data['name']:
            raise InputValidationError('Name is required')
        if 'age' not in self.data or not isinstance(self.data['age'], int):
            raise InputValidationError('Age must be a valid integer')

    def process(self):
        try:
            self.validate_input()
            # Processing logic here
            result = {'status': 'success', 'data': self.data}
            return json.dumps(result)
        except InputValidationError as e:
            return json.dumps({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    input_data = {'name': 'John', 'age': 30}
    processor = DataProcessor(input_data)
    print(processor.process())