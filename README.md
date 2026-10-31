# python-utils-35

`python-utils-35` is a high-performance, cross-platform autoclicker library built on `pynput` for seamless automation. It provides a lightweight API for executing rapid mouse events with customizable intervals and trigger conditions.

## Features
*   **Precision Timing:** Supports micro-second interval delays to simulate high-frequency click streams.
*   **Dynamic Triggers:** Configurable keyboard shortcuts to toggle automation state without interrupting the main process.
*   **Coordinate Support:** Capability to lock clicks to a specific screen position or follow the current cursor location.
*   **Thread-Safe Execution:** Runs automation in a background daemon thread to maintain responsiveness of your primary application.

## Installation

Ensure you have Python 3.7+ installed. Install the package directly via pip:

```bash
pip install python-utils-35
```

For development installations, clone the repository and run:

```bash
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35
pip install -e .
```

## Usage Example

The following script initializes an autoclicker that triggers a left-click every 0.5 seconds, controlled by the `F8` key.

```python
from utils_35 import AutoClicker

# Initialize with a 0.5-second interval
clicker = AutoClicker(interval=0.5, button='left')

# Start the automation process
clicker.start()

# Stop after 10 seconds of activity
import time
time.sleep(10)
clicker.stop()
```

## Contributing
Contributions are welcome. Please open an issue or submit a pull request if you encounter bugs or have feature requests. 

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the `LICENSE` file for details.