import logging
import os

# Configuration constants with validation paths
DEFAULT_CLICK_INTERVAL = 0.05
MIN_INTERVAL = 0.001
MAX_INTERVAL = 60.0

# Logging configuration constants
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.INFO

# Default system path definitions
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.path.join(BASE_DIR, 'settings.json')

# Error handling status codes
STATUS_SUCCESS = 0
STATUS_INVALID_INPUT = 1
STATUS_PERMISSION_DENIED = 2
STATUS_OS_ERROR = 3

# Supported mouse button mapping
MOUSE_BUTTONS = {
    'left': 'left',
    'right': 'right',
    'middle': 'middle'
}

def get_safe_interval(interval: float) -> float:
    """Clamps interval within acceptable bounds to prevent system hangs."""
    if not isinstance(interval, (int, float)):
        return DEFAULT_CLICK_INTERVAL
    
    return max(MIN_INTERVAL, min(float(interval), MAX_INTERVAL))

# Default application state
DEFAULT_STATE = {
    'enabled': False,
    'interval': DEFAULT_CLICK_INTERVAL,
    'button': 'left'
}