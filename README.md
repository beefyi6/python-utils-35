# python-utils-35

A high-performance, cross-platform autoclicker library built for automation and task efficiency. This utility provides a clean programmatic interface for simulating mouse input with precision timing control.

## Features

*   **Jitter Compensation:** Includes configurable randomized intervals to mimic human-like clicking behavior and avoid detection.
*   **Dynamic Targeting:** Supports coordinate-based clicking or image recognition triggers to automate interactions with specific UI elements.
*   **Hotkey Integration:** Built-in listener support to start or pause clicking sequences via global keyboard shortcuts.
*   **Resource Optimized:** Utilizes low-level system APIs to ensure minimal CPU overhead during extended background execution.

## Installation

Ensure you have Python 3.8+ installed. You can install the package dependencies directly via pip:

```bash
git clone https://github.com/Developer/python-utils-35
cd python-utils-35
pip install -r requirements.txt
```

## Basic Usage

You can initialize an autoclicker instance and trigger it with a set delay in milliseconds. The following example demonstrates a basic implementation:

```python
from utils import AutoClicker

# Initialize with 100ms interval
clicker = AutoClicker(interval=0.1)

# Start clicking at current mouse position
clicker.start()

# Stop after 5 seconds
import time
time.sleep(5)
clicker.stop()
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.