import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name='autoclicker', log_file='app.log', level=logging.INFO):
    """Initializes a rotating file logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    # Rotation settings: 5MB per file, max 3 files
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    
    # Also log to console for development visibility
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger