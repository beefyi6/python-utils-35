import os
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "autoclicker.log"
DEFAULT_FORMAT = "%(asctime)s - %(name)s - [%(levelname)s] - %(message)s"


def setup_logger(
    name: str = "autoclicker",
    log_file: Optional[Path] = None,
    level: int = logging.INFO,
    max_bytes: int = 1_048_576,  # 1 MB log limit
    backup_count: int = 5,
) -> logging.Logger:
    """Configure and return a logger instance with rotating file and stream handlers."""
    target_file = log_file or LOG_FILE
    target_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear handlers to avoid duplicated log entries on re-initialization
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(DEFAULT_FORMAT)

    # File rotation prevents log inflation during high-frequency clicking
    file_handler = RotatingFileHandler(
        target_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console output handler for live execution monitoring
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger


# Shared instance for application-wide click event logging
click_logger = setup_logger()
