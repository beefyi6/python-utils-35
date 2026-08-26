# python-utils-35

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

`python-utils-35` is a high-performance, lightweight asynchronous autoclicker built purely in Python. Designed for automation tasks, it provides precise timing control and minimal CPU overhead through direct system API hooks.

## Features

- **Sub-Millisecond Precision**: Leverages high-resolution performance counters to ensure consistent CPS (clicks per second) rates without thread sleeping drift.
- **Configurable Patterns**: Supports fixed intervals, randomized human-like delays, and customizable burst firing to bypass basic rate-limiting detection.
- **Global Hotkey Integration**: Easily toggle clicking states on the fly using customizable keyboard shortcuts without needing focus on the target window.
- **Multi-Button Mapping**: Configure automated triggers for Left, Right, and Middle mouse buttons independently.

## Installation

Ensure you have Python 3.8 or higher installed on your system. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35
pip install -r requirements.txt
```

*(Note: Depending on your operating system, administrative privileges or accessibility permissions may be required for global input monitoring).*

## Usage

Here is a basic script to run the autoclicker with a fixed interval of 50 milliseconds (20 CPS) toggled by the `F6` key.

```python
from utils35 import AutoClicker, MouseButton

# Initialize the autoclicker
# delay in seconds (0.05s = 50ms), targeting the left mouse button
clicker = AutoClicker(
    delay=0.05, 
    button=MouseButton.LEFT, 
    toggle_key="f6"
)

if __name__ == "__main__":
    print("Autoclicker initialized. Press F6 to start/stop. Press Ctrl+C to exit.")
    clicker.start()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs or feature requests.

## License

This project is open-source and available under the [MIT License](LICENSE).