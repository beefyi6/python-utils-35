# python-utils-35

A high-performance, cross-platform autoclicker built in Python. This utility provides precise automation for repetitive mouse tasks with minimal system overhead.

## Features
*   **Customizable Intervals:** Set exact click speeds with support for millisecond-level precision.
*   **Dynamic Triggering:** Bind clicking actions to specific hotkeys for seamless start/stop control.
*   **Click Patterns:** Choose between single clicks, double-click bursts, or hold-to-click functionality.
*   **Optimized Performance:** Uses low-level system hooks to ensure consistent performance even under heavy CPU load.

## Installation

Ensure you have [Python 3.8+](https://www.python.org/) installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35
pip install -r requirements.txt
```

## Usage

To start the autoclicker with default settings (10 clicks per second), execute the following command in your terminal:

```bash
python main.py --interval 0.1
```

You can customize the button behavior and hotkey via command-line arguments:

```bash
# Set interval to 50ms and bind start/stop to the 'F6' key
python main.py --interval 0.05 --hotkey 'f6'
```

Press `Ctrl+C` in the terminal to terminate the application safely at any time.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.