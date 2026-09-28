# python-utils-35

`python-utils-35` is a high-performance, cross-platform automation library built to simulate complex mouse interactions with minimal overhead. It provides a clean, Pythonic API for developers needing precise click control in desktop environments.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

*   **Precision Timing:** Supports microsecond-accurate intervals between clicks to bypass basic input-rate filtering.
*   **Coordinate-Based Mapping:** Easily target specific screen regions or dynamic elements using relative or absolute coordinates.
*   **Multi-Button Support:** Native handling for primary, secondary, and middle mouse buttons, including complex drag-and-drop event sequences.
*   **Safe-Guard Interrupts:** Integrated failsafe detection that triggers an emergency stop when the mouse is moved to a corner of the screen.

## Installation

Ensure you have Python 3.8+ installed. You can install the package directly via pip:

```bash
pip install python-utils-35
```

For development builds, clone the repository and install dependencies:

```bash
git clone https://github.com/Developer/python-utils-35.git
cd python-utils-35
pip install -r requirements.txt
```

## Usage

Here is a quick example of how to initialize a rapid-click sequence at a specific coordinate:

```python
from pyutils35 import AutoClicker

# Initialize the clicker
bot = AutoClicker(interval=0.01)

# Perform 50 clicks at coordinates (500, 500)
bot.click(x=500, y=500, clicks=50)

# Execute a drag operation from A to B
bot.drag(start=(100, 100), end=(200, 200), duration=0.5)
```

## Contributing
Contributions are welcome! Please open an issue to discuss proposed features or submit a pull request with unit tests for any bug fixes.

## License
Distributed under the MIT License. See `LICENSE` for more information.