import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'autoclicker.log') -> logging.Logger:
    """
    Configures a rotating file logger for the application.
    Limits file size to 1MB and keeps 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate files at 1MB, keeping 3 old logs
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=1*1024*1024, 
            backupCount=3
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Optional console output for debugging
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)

    return logger