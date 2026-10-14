from typing import Optional

class AutoClickerError(Exception):
    """Base exception for the python-utils-35 package."""
    pass

class ConfigurationError(AutoClickerError):
    """Raised when the clicker configuration is invalid."""
    def __init__(self, message: str, field: Optional[str] = None) -> None:
        self.field = field
        super().__init__(f"{message} (field: {field})" if field else message)

class ClickExecutionError(AutoClickerError):
    """Raised during failures in the clicking event loop."""
    def __init__(self, message: str, code: int = 1) -> None:
        self.code = code
        super().__init__(f"{message} [Error Code: {code}]")

class PermissionDeniedError(AutoClickerError):
    """Raised when the script lacks required system OS access."""
    def __init__(self, message: str = "Insufficient privileges for input control") -> None:
        super().__init__(message)