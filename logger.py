import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='autoclicker', log_file='autoclicker.log', level=logging.INFO):
    """Configures a rotating file logger for session monitoring."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if function called multiple times
    if not logger.handlers:
        # 5MB per file, keep 3 historical log files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=5 * 1024 * 1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Add console output for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instantiate default logger for the project
logger = setup_logger()