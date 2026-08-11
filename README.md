# python-utils-35

A collection of utility functions designed to enhance the productivity of Python developers. This library simplifies common tasks such as data manipulation, file handling, and string processing with minimal setup.

## Features
- **Data Handling**: Quickly convert lists and dictionaries to JSON and vice versa with error handling.
- **File Operations**: Efficiently read and write to CSV files with automatic header generation and type inference.
- **String Utilities**: Transform strings with functions for trimming, case conversion, and searching with regex support.
- **Custom Logging**: Implement a simple logger that can be easily configured to output messages to files or the console.

## Installation

To install the package, you can use pip. Run the following command in your terminal:

```bash
pip install python-utils-35
```

## Basic Usage Example

Here's a simple example demonstrating how to use some of the utilities provided by the `python-utils-35` library:

```python
from utils import JsonUtils, FileUtils, StringUtils, Logger

# Initialize logger
logger = Logger('app.log')
logger.info("Starting the utility example.")

# JSON Example
data = {'name': 'John', 'age': 30}
json_data = JsonUtils.to_json(data)
logger.info(f"Converted data to JSON: {json_data}")

# File Operation Example
FileUtils.write_csv('output.csv', [['Name', 'Age'], ['Alice', 28], ['Bob', 32]])
logger.info("CSV file created successfully.")

# String Utility Example
result = StringUtils.capitalize("hello world!")
logger.info(f"Capitalized String: {result}")
```

This concise collection of functions provides a robust framework to streamline developer tasks while maintaining clarity and usability. For further details, please refer to the documentation.

![License](https://img.shields.io/badge/license-MIT-green)