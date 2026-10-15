from typing import Optional

class AutoclickerError(Exception):
    """Base exception for all autoclicker operations."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when the configuration file is invalid or missing."""
    def __init__(self, message: str, config_path: Optional[str] = None) -> None:
        self.config_path = config_path
        super().__init__(f"{message} (Path: {config_path})")

class ClickerRuntimeError(AutoclickerError):
    """Raised during mouse event execution failures."""
    def __init__(self, message: str, code: int = 1) -> None:
        self.code = code
        super().__init__(f"{message} (Error code: {code})")

class ValidationError(AutoclickerError):
    """Raised when user input fails boundary validation."""
    def __init__(self, field: str, value: any) -> None:
        self.field = field
        self.value = value
        super().__init__(f"Invalid value '{value}' for field '{field}'")