import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "autoclicker", log_file: str = "autoclicker.log") -> logging.Logger:
    """Configure and return a rotating file logger for the autoclicker."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Prevent duplicate handlers if setup is called multiple times
    if logger.handlers:
        return logger

    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Setup rotating file handler (5 MB per file, max 3 backup files)
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5 * 1024 * 1024, 
        backupCount=3
    )
    handler.setLevel(logging.INFO)

    # Define log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)
    
    return logger
