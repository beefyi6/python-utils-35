# python-utils-35

A high-performance, lightweight autoclicker utility designed for precision automation in Python. This tool leverages `pynput` to simulate system-level mouse events with customizable intervals and trigger patterns.

## Features

*   **Configurable Interval:** Set specific delays between clicks (in milliseconds) to match target application requirements.
*   **Toggle System:** Bind start/stop functionality to custom hotkeys for seamless background execution.
*   **Variable Click Modes:** Supports left, right, and middle button clicks, alongside single or double-click automation.
*   **Anti-Detection Buffer:** Implements a randomized jitter feature to mimic human-like interaction patterns.

## Installation

Ensure you have Python 3.7+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35
pip install -r requirements.txt
```

## Usage

To launch the autoclicker with default settings, run the following command:

```bash
python main.py --interval 0.5 --button left
```

### Simple Script Example

You can also import the core utility into your own scripts to trigger clicks programmatically:

```python
from utils.clicker import AutoClicker

# Initialize with a 100ms delay
clicker = AutoClicker(interval=0.1)

# Start clicking at the current cursor position
clicker.start()

# Stop clicking after a specific duration
clicker.stop()
```

## Contributing
Contributions are welcome. Please submit a pull request with clear documentation of your changes or open an issue for bug reporting.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.