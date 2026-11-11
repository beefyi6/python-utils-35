# python-utils-35

A high-performance, cross-platform autoclicker library built with Python. Designed for precision automation and repetitive task execution with minimal CPU overhead.

## Features

*   **Configurable Intervals:** Precise millisecond-level delay settings for optimized clicking speeds.
*   **Dynamic Targeting:** Built-in coordinate detection to target specific UI elements automatically.
*   **Multi-Button Support:** Full support for left, right, and middle mouse button simulation.
*   **Hotkeys & Safety:** Integrated emergency stop sequences to ensure control during automated execution.

## Installation

Ensure you have Python 3.8+ installed. You can install the package directly via pip:

```bash
# Clone the repository
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

To launch a basic autoclicker instance, initialize the `Clicker` class and define your click frequency:

```python
from utils import Autoclicker

# Initialize with 100ms interval
bot = Autoclicker(interval=0.1)

# Start clicking at the current mouse position
bot.start()

# Stop after 10 seconds
bot.stop(after=10)
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.