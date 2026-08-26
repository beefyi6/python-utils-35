class AutoclickerError(Exception):
    """Base exception for all autoclicker errors."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when configuration data is invalid or missing."""
    def __init__(self, message: str, key: str = None):
        super().__init__(message)
        self.key = key

class DataProcessingError(AutoclickerError):
    """Raised when click sequence or timing data cannot be parsed."""
    def __init__(self, message: str, raw_data: any = None):
        super().__init__(message)
        self.raw_data = raw_data

class ClickExecutionError(AutoclickerError):
    """Raised when the OS simulation of clicks or movement fails."""
    def __init__(self, message: str, coordinates: tuple = None):
        super().__init__(message)
        self.coordinates = coordinates
