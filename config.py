import logging
from logging.handlers import RotatingFileHandler
import os
def setup_logger(log_file="autoclicker.log", level=logging.INFO, max_bytes=1024*1024, backup_count=5):
    """Configure logger with rotating file handler for autoclicker."""
    logger = logging.getLogger("autoclicker")
    # Prevent duplicate handlers on repeated calls
    if logger.hasHandlers():
        return logger
    logger.setLevel(level)
    # Create directory for log file if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # Rotating file handler limits size and keeps backups
    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_handler.setLevel(level)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

logger = setup_logger()