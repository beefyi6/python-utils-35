import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str, log_file: str = 'autoclicker.log') -> logging.Logger:
    """Configures a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if logger is re-initialized
    if not logger.handlers:
        # Format: timestamp - name - level - message
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Rotate after 1MB, keep 3 backup files
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=1*1024*1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Default instance for the autoclicker module
clicker_logger = setup_logger('autoclicker')