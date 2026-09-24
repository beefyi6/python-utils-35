import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str = 'autoclicker.log') -> logging.Logger:
    """Configures a rotating file logger for the autoclicker."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if function is called multiple times
    if not logger.handlers:
        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Rotation: 1MB per file, keep 3 backup files
        handler = RotatingFileHandler(
            log_file, 
            maxBytes=1*1024*1024, 
            backupCount=3
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Also output to console for better visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger