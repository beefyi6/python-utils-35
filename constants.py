from enum import Enum


class MouseButton(Enum):
    """Mouse buttons supported by the autoclicker engine."""
    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"


class ClickType(Enum):
    """Types of click actions available."""
    SINGLE = "single"
    DOUBLE = "double"
    HOLD = "hold"


# Default timing values in seconds
DEFAULT_INTERVAL_SECONDS = 0.1
MIN_ALLOWED_INTERVAL = 0.001
MAX_ALLOWED_INTERVAL = 86400.0  # 24 hours

# Failsafe and control defaults
DEFAULT_HOTKEY_TOGGLE = "f6"
DEFAULT_HOTKEY_STOP = "f7"
FAILSAFE_CORNER_PADDING_PX = 10

# Common timing presets (label -> seconds)
SPEED_PRESETS = {
    "ultra_fast": 0.005,
    "fast": 0.05,
    "normal": 0.2,
    "slow": 1.0,
}


def get_preset_interval(preset_name: str) -> float:
    """Return the interval in seconds for a known preset name."""
    return SPEED_PRESETS.get(preset_name.lower(), DEFAULT_INTERVAL_SECONDS)
