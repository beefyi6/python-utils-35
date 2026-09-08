import platform

# Application configuration constants
APP_NAME = "python-utils-35"
VERSION = "1.0.0"

# Mouse action constants
LEFT_BUTTON = "left"
RIGHT_BUTTON = "right"
MIDDLE_BUTTON = "middle"

# Default operation timings
DEFAULT_INTERVAL = 0.1
MAX_CLICK_RATE_LIMIT = 0.001

# System specific pathing and configurations
IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"
IS_MACOS = platform.system() == "Darwin"

# Error and log patterns
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE_NAME = "autoclicker.log"

# User interaction constants
DEFAULT_HOTKEY = "f6"
STOP_HOTKEY = "f7"

def get_supported_buttons():
    """Returns list of supported mouse buttons."""
    return [LEFT_BUTTON, RIGHT_BUTTON, MIDDLE_BUTTON]

if __name__ == "__main__":
    print(f"Loaded {APP_NAME} constants for {platform.system()}")