class AutoclickerError(Exception):
    """Base exception for the application."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when config validation fails."""
    pass

class ClickerRuntimeError(AutoclickerError):
    """Raised during click execution failures."""
    pass

class DeviceNotFoundError(AutoclickerError):
    """Raised when input devices are unreachable."""
    pass

def raise_if_none(value, message, exception_type=AutoclickerError):
    """Helper to enforce non-null arguments."""
    if value is None:
        raise exception_type(message)
    return value

def validate_coordinate(x, y):
    """Ensures screen coordinates are non-negative."""
    if x < 0 or y < 0:
        raise ConfigurationError(f"Invalid coordinates: ({x}, {y})")
    return True