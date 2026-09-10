class AutoClickerError(Exception):
    """Base exception for all auto-clicker related errors."""
    pass

class CoordinateOutOfBoundsError(AutoClickerError):
    """Raised when click coordinates fall outside screen bounds."""
    def __init__(self, x, y):
        super().__init__(f"Coordinates ({x}, {y}) are outside the valid screen area.")

class ProcessNotFoundError(AutoClickerError):
    """Raised when the target application process is missing."""
    def __init__(self, process_name):
        super().__init__(f"Target process '{process_name}' could not be found.")

class PermissionDeniedError(AutoClickerError):
    """Raised when lacking OS-level permissions for input simulation."""
    def __init__(self, action):
        super().__init__(f"Insufficient privileges to perform action: {action}.")

class ConfigurationError(AutoClickerError):
    """Raised when configuration settings are invalid or missing."""
    def __init__(self, setting):
        super().__init__(f"Invalid configuration detected for: {setting}.")

def raise_if_out_of_bounds(x, y, max_x, max_y):
    """Validates screen coordinates against maximum display dimensions."""
    if not (0 <= x <= max_x and 0 <= y <= max_y):
        raise CoordinateOutOfBoundsError(x, y)