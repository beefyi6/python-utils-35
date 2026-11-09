import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = 'autoclicker', log_file: str = 'app.log'):
    """
    Configures a rotating file logger for the application.
    Max file size is 1MB, keeping up to 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if called multiple times
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotating file handler (1MB limit)
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=1*1024*1024, 
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        # Console stream handler for immediate feedback
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

# Default project logger instance
logger = setup_logger()