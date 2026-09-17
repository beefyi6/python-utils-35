# python-utils-35

A high-performance, lightweight autoclicker utility built with Python. Designed for automation tasks, this tool provides precise control over click intervals and mouse coordinates with minimal system overhead.

## Features

*   **Configurable Intervals:** Set precise millisecond delays between clicks to match specific task requirements.
*   **Coordinate Targeting:** Supports both dynamic "follow mouse" mode and fixed-point execution.
*   **Hotkey Integration:** Start and stop automation instantly using global keyboard listeners.
*   **Low CPU Footprint:** Optimized threading model ensures the script remains responsive while running in the background.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed, then clone the repository and install the dependencies:

```bash
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35
pip install -r requirements.txt
```

## Usage

To run the autoclicker with default settings (100ms interval), execute the following command in your terminal:

```bash
python main.py --interval 100
```

### Basic Script Example
You can also import the core utility into your own Python projects:

```python
from utils import AutoClicker

# Initialize clicker with 500ms delay
bot = AutoClicker(interval=0.5)

# Start clicking at the current mouse position
bot.start()

# Stop after 10 seconds
import time
time.sleep(10)
bot.stop()
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.