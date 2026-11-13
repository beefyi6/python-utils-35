class AutoclickerError(Exception):
    """Base exception for all autoclicker-related issues."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when the autoclicker configuration is invalid."""
    pass

class HardwareInputError(AutoclickerError):
    """Raised when low-level input injection fails."""
    pass

class ProcessInterrupt(AutoclickerError):
    """Raised when the autoclicker process is force stopped."""
    def __init__(self, message: str = "Execution interrupted by user") -> None:
        super().__init__(message)

class SafetyTriggerError(AutoclickerError):
    """Raised when a fail-safe mechanism is activated."""
    def __init__(self, trigger_type: str) -> None:
        self.trigger_type: str = trigger_type
        super().__init__(f"Safety trigger activated: {trigger_type}")