# python-utils-35

A high-performance, lightweight autoclicker utility designed for Python automation tasks. This tool provides precise mouse control and configurable click patterns for repetitive workflow efficiency.

## Features

*   **Configurable Click Rate:** Set specific millisecond intervals or randomization parameters to simulate human-like behavior.
*   **Dynamic Targeting:** Easily target specific coordinates on your screen or follow the current cursor position.
*   **Hotkey Integration:** Start or stop automation instantly using customizable global keyboard shortcuts.
*   **Low Resource Footprint:** Optimized for minimal CPU usage, allowing it to run reliably in the background during long tasks.

## Installation

Ensure you have Python 3.8+ installed. Install the required dependencies using pip:

```bash
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35
pip install -r requirements.txt
```

## Usage

You can launch the clicker from the terminal by specifying the click interval (in seconds) and the number of repetitions.

```python
# Example: Click once every 0.5 seconds, 100 times
python main.py --interval 0.5 --count 100
```

For advanced users, you can import the core logic into your own scripts:

```python
from utils import AutoClicker

clicker = AutoClicker(interval=0.2)
clicker.start()
```

*Note: Ensure you have the necessary system permissions to control mouse input on your operating system.*

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.