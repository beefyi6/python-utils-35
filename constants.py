from typing import Tuple

# General constants used in the autoclicker application
MAX_CLICKS: int = 1000  # Maximum number of clicks allowed
CLICK_DELAY: float = 0.1  # Delay between clicks in seconds
DEFAULT_CLICK_POSITION: Tuple[int, int] = (100, 200)  # Default position to click

# Hotkey constants for starting and stopping the autoclicker
START_HOTKEY: str = 'ctrl+shift+s'  # Hotkey to start the autoclicker
STOP_HOTKEY: str = 'ctrl+shift+x'  # Hotkey to stop the autoclicker

# Possible states of the autoclicker
class ClickerState:
    NOT_RUNNING = 0  # Autoclicker is not running
    RUNNING = 1      # Autoclicker is currently running
    STOPPED = 2      # Autoclicker has been stopped

# Other configuration constants
WINDOW_TITLE: str = 'Autoclicker'  # Title of the autoclicker window
