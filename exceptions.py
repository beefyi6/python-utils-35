class AutoClickerError(Exception):
    """Base class for exceptions in AutoClicker."""
    pass

class ClickLimitExceededError(AutoClickerError):
    """Raised when click limit is exceeded."""
    def __init__(self, limit):
        self.limit = limit
        super().__init__(f'Click limit of {limit} exceeded.')

class InvalidClickIntervalError(AutoClickerError):
    """Raised when an invalid click interval is provided."""
    def __init__(self, interval):
        self.interval = interval
        super().__init__(f'Invalid click interval: {interval}. Must be positive.')

class ClickerNotRunningError(AutoClickerError):
    """Raised when clicker operations are attempted while not running."""
    pass

class ConfigurationError(AutoClickerError):
    """Raised for invalid configuration settings."""
    def __init__(self, message):
        super().__init__(message)