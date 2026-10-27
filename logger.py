import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path


def setup_logger(
    name: str = "autoclicker",
    log_file: str = "autoclicker.log",
    max_bytes: int = 1_048_576,  # 1 MB per log file
    backup_count: int = 3,
    level: int = logging.INFO
) -> logging.Logger:
    """Configures and returns a logger with console and rotating file outputs."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if function is called multiple times
    if logger.handlers:
        return logger

    # Common log format for click events and system status
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Ensure log directory exists
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    # File handler with size-based log rotation
    file_handler = RotatingFileHandler(
        log_dir / log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    # Console handler for real-time output during script execution
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    return logger


# Initialize default logger instance for click automation tracking
logger = setup_logger()
