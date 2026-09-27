from enum import Enum, unique

@unique
class MouseButton(str, Enum):
    """Supported mouse buttons for the autoclicker."""
    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"

@unique
class ClickType(str, Enum):
    """Types of click actions supported."""
    SINGLE = "single"
    DOUBLE = "double"
    HOLD = "hold"

# Default operation settings
DEFAULT_INTERVAL_SECONDS: float = 0.1
DEFAULT_CLICK_TYPE: ClickType = ClickType.SINGLE
DEFAULT_MOUSE_BUTTON: MouseButton = MouseButton.LEFT
DEFAULT_CLICK_COUNT: int = 0  # 0 indicates infinite looping

# System control hotkeys
DEFAULT_START_HOTKEY: str = "f7"
DEFAULT_STOP_HOTKEY: str = "f8"

# Validation constraints and limits
MIN_INTERVAL_SECONDS: float = 0.001
MAX_INTERVAL_SECONDS: float = 3600.0
MIN_CLICK_COUNT: int = 0
MAX_CLICK_COUNT: int = 999999
