import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='autoclicker', log_file='app.log', level=logging.INFO):
    """
    Configures a rotating file logger for the application.
    Limits file size to 1MB and keeps 3 backups.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # Format logs with timestamp, logger name, level, and message
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate logs after 1MB, keeping 3 historical files
        handler = RotatingFileHandler(
            log_file, maxBytes=1_000_000, backupCount=3
        )
        handler.setFormatter(formatter)

        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(console_handler)

    return logger

# Instantiate default logger for use across the package
logger = setup_logger()