class AutoclickerError(Exception):
    """Base exception for the autoclicker utility."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when settings are invalid or missing."""
    pass

class InputDeviceError(AutoclickerError):
    """Raised when mouse or keyboard control fails."""
    pass

class ValidationError(AutoclickerError):
    """Raised when input parameters fall outside bounds."""
    pass

def validate_click_interval(interval: float):
    """Ensures click interval is within safe operating range."""
    if not isinstance(interval, (int, float)):
        raise ValidationError(f"Interval must be numeric, got {type(interval)}")
    if interval < 0.01:
        raise ValidationError("Interval too low; risk of system instability")
    if interval > 60.0:
        raise ValidationError("Interval too high; likely unintended usage")

def handle_device_fault(e: Exception):
    """Standardized response to input device failures."""
    if isinstance(e, PermissionError):
        raise InputDeviceError("Insufficient permissions to control system hardware") from e
    raise InputDeviceError(f"Unexpected hardware failure: {str(e)}") from e