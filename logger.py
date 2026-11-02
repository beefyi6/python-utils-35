import logging
import sys
from datetime import datetime

# Configure global logging for the autoclicker utility
def get_logger(name: str) -> logging.Logger:
    """Initializes a logger with standard formatting."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def log_click_event(logger: logging.Logger, x: int, y: int, button: str) -> None:
    """Logs click coordinates and button type."""
    logger.info(f"action performed at ({x}, {y}) using {button} button")

def log_error(logger: logging.Logger, error: Exception) -> None:
    """Standardizes exception logging format."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.error(f"[{timestamp}] unexpected failure: {str(error)}")