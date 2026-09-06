class AutoclickerError(Exception):
    """Base exception class for the autoclicker."""
    pass

class HardwareInteractionError(AutoclickerError):
    """Raised when low-level input simulation fails."""
    pass

class ConfigurationValidationError(AutoclickerError):
    """Raised when user settings are invalid."""
    pass

class PerformanceThresholdExceeded(AutoclickerError):
    """Raised when click interval is below safe thresholds."""
    def __init__(self, interval, min_safe):
        super().__init__(f"Interval {interval}ms is below safe limit of {min_safe}ms")

def validate_interval(interval: float, min_safe: float = 10.0) -> None:
    """Performance guardrail to prevent system CPU exhaustion."""
    if interval < min_safe:
        raise PerformanceThresholdExceeded(interval, min_safe)

class EventStreamInterrupt(AutoclickerError):
    """Custom exception to handle graceful event stream termination."""
    pass