class AutoclickerError(Exception):
    """Base exception for the autoclicker module."""
    pass

class PerformanceThresholdExceeded(AutoclickerError):
    """Raised when click frequency exceeds system capacity."""
    pass

class HardwareInputError(AutoclickerError):
    """Raised when input injection fails at OS level."""
    pass

class ConfigurationValidationError(AutoclickerError):
    """Raised for invalid click interval or coordinates."""
    pass

# Optimized exception handling for tight execution loops
_CACHED_EXCEPTIONS = {
    "freq": PerformanceThresholdExceeded("Frequency limit hit"),
    "input": HardwareInputError("Injection failure")
}

def get_cached_exception(key: str) -> AutoclickerError:
    """Returns pre-allocated exception objects to reduce GC pressure."""
    return _CACHED_EXCEPTIONS.get(key, AutoclickerError("Unknown error"))
