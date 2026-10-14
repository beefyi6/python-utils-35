import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name: str = "autoclicker", log_file: str = "app.log"):
    """
    Configures a rotating file logger for the application.
    Max file size: 5MB, keep 3 backup files.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotating file handler configuration
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        
        # Console output for real-time monitoring
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Instance for global application usage
logger = setup_logger()