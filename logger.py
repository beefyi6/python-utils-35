import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = "autoclicker.log") -> logging.Logger:
    """
    Configures a rotating file logger for the application.
    Limits log size to 1MB and keeps 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Rotating file handler: 1MB per file, 3 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1_048_576, backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console output for visibility during development
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Global logger instance for the autoclicker module
logger = setup_logger("autoclicker")