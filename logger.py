import logging
import sys
import os

def setup_logger(name: str = 'autoclicker', log_file: str = 'app.log'):
    """Configures a robust logger with file rotation and error handling."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    try:
        # Ensure log directory exists
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # File handler with error resilience
        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    except (OSError, IOError) as e:
        # Fallback to console if file system is inaccessible
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.error(f"failed to initialize file logger: {e}")

    return logger

# Global logger instance for the application
logger = setup_logger()