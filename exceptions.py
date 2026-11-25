class AutoclickerError(Exception):
    """Base exception class for the autoclicker."""
    pass

class ClickExecutionError(AutoclickerError):
    """Raised when the click simulation fails."""
    pass

class HardwareAbstractionError(AutoclickerError):
    """Raised when low-level driver interaction fails."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised for invalid user-defined settings."""
    pass

def handle_exception(exc: Exception) -> None:
    """Standardized logging wrapper for exceptions."""
    if isinstance(exc, AutoclickerError):
        print(f"[CRITICAL] {type(exc).__name__}: {exc}")
    else:
        print(f"[UNEXPECTED] {exc}")

class PerformanceBottleneckError(AutoclickerError):
    """Raised when click interval exceeds processing latency."""
    def __init__(self, interval: float, latency: float):
        self.message = f"Interval {interval}s shorter than latency {latency}s"
        super().__init__(self.message)