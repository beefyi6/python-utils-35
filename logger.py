import logging
import sys
from typing import Optional

class ClickerLogger:
    """Handles logging for the autoclicker application."""

    def __init__(self, name: str = "autoclicker", level: int = logging.INFO) -> None:
        """Initialize the logger with a specific name and level."""
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        
        if not self.logger.handlers:
            self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Log error messages with optional exception details."""
        if exc:
            self.logger.error(f"{message}: {exc}", exc_info=True)
        else:
            self.logger.error(message)

    def debug(self, message: str) -> None:
        """Log debug level messages."""
        self.logger.debug(message)

# Global instance for easy access across the package
logger = ClickerLogger()