class AutoClickerException(Exception):
    """Base class for all exceptions raised by the autoclicker."""
    pass

class InvalidConfigurationError(AutoClickerException):
    """Exception raised for invalid configurations."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ClickRateExceededError(AutoClickerException):
    """Exception raised when the click rate exceeds the limit."""
    def __init__(self, threshold):
        self.threshold = threshold
        self.message = f"Click rate exceeds limit of {self.threshold} clicks per second."
        super().__init__(self.message)

class ClickIntervalError(AutoClickerException):
    """Exception raised for invalid click intervals."""
    def __init__(self, interval):
        self.interval = interval
        self.message = f"Click interval of {self.interval} seconds is invalid."
        super().__init__(self.message)