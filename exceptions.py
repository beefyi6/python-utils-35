"""Custom exception hierarchy for the autoclicker module."""


class AutoClickerError(Exception):
    """Base exception class for all autoclicker errors."""

    def __init__(self, message: str = "An autoclicker error occurred"):
        self.message = message
        super().__init__(self.message)


class ConfigurationError(AutoClickerError):
    """Raised when provided autoclicker settings or arguments are invalid."""

    def __init__(self, parameter: str, value: object, reason: str = ""):
        self.parameter = parameter
        self.value = value
        details = f": {reason}" if reason else ""
        msg = f"Invalid configuration for '{parameter}' = {value!r}{details}"
        super().__init__(msg)


class ClickerStateError(AutoClickerError):
    """Raised when an operation is performed in an invalid clicker state."""

    pass


class FailsafeTriggeredError(AutoClickerError):
    """Raised when the emergency stop failsafe mechanism is activated."""

    def __init__(self, position: tuple[int, int] | None = None):
        self.position = position
        msg = "Failsafe triggered by user interaction"
        if position:
            msg += f" at coordinates {position}"
        super().__init__(msg)


class InputPermissionError(AutoClickerError):
    """Raised when OS permissions block simulated mouse or keyboard input."""

    def __init__(self, action: str = "simulating input"):
        super().__init__(f"Permission denied while {action}")
