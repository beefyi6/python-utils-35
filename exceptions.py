from typing import Optional

class AutoClickerError(Exception):
    """Base exception for all auto-clicker operations."""
    pass

class ConfigurationError(AutoClickerError):
    """Raised when the clicker configuration is invalid."""
    def __init__(self, message: str, field: Optional[str] = None) -> None:
        super().__init__(message)
        self.field = field

class ClickExecutionError(AutoClickerError):
    """Raised when a mouse or keyboard event fails."""
    pass

class InterruptionError(AutoClickerError):
    """Raised when the execution is stopped by the user."""
    pass

def raise_if_invalid(condition: bool, message: str) -> None:
    """Utility to trigger configuration errors if conditions are not met."""
    if not condition:
        raise ConfigurationError(message)

class DeviceNotReadyError(AutoClickerError):
    """Raised when input hardware is not responding."""
    def __init__(self, device_id: int) -> None:
        super().__init__(f"Device {device_id} is currently unavailable.")
        self.device_id = device_id