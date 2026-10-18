class AutoclickerError(Exception):
    """Base exception for the autoclicker."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when config values are invalid."""
    pass

class InputDeviceError(AutoclickerError):
    """Raised when mouse or keyboard control fails."""
    pass

class ExecutionTimeoutError(AutoclickerError):
    """Raised when an action exceeds the time limit."""
    pass

def validate_click_interval(interval: float):
    """Ensures click interval is within safe operational bounds."""
    if interval < 0.01:
        raise ConfigurationError(f"Interval {interval}s too low: risk of system lag")
    if interval > 3600:
        raise ConfigurationError(f"Interval {interval}s too high: potential user error")

def handle_device_failure(error: Exception):
    """Standardized response to input hardware interaction failures."""
    if isinstance(error, PermissionError):
        raise InputDeviceError("Insufficient privileges for system input control") from error
    raise InputDeviceError("Unexpected hardware communication failure") from error