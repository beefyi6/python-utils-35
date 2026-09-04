"""Custom exception classes for the autoclicker application."""


class AutoClickerError(Exception):
    """Base exception class for all autoclicker errors."""
    pass


class InvalidClickIntervalError(AutoClickerError):
    """Raised when the specified click interval is invalid or unsafe."""

    def __init__(self, interval: float, min_interval: float = 0.001):
        self.interval = interval
        self.min_interval = min_interval
        super().__init__(
            f"Click interval {interval}s is invalid. Minimum allowed is {min_interval}s."
        )


class CoordinatesOutOfBoundsError(AutoClickerError):
    """Raised when target click coordinates fall outside screen boundaries."""

    def __init__(self, x: int, y: int, screen_width: int, screen_height: int):
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        super().__init__(
            f"Coordinates ({x}, {y}) out of screen bounds ({screen_width}x{screen_height})."
        )


class ClickSequenceError(AutoClickerError):
    """Raised when loading or parsing click sequence data fails."""

    def __init__(self, message: str, line_number: int = None):
        self.line_number = line_number
        location = f" at line {line_number}" if line_number is not None else ""
        super().__init__(f"Failed to process click sequence{location}: {message}")


class HotKeyConflictError(AutoClickerError):
    """Raised when configured hotkeys conflict with reserved system keys."""

    def __init__(self, hotkey: str):
        self.hotkey = hotkey
        super().__init__(f"Hotkey binding '{hotkey}' conflicts with reserved shortcuts.")
