import logging
import sys
from datetime import datetime

def setup_logger(name: str, log_file: str = 'autoclicker.log') -> logging.Logger:
    """Configures a standardized logger for the application."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setFormatter(formatter)
    logger.addHandler(c_handler)

    # File handler
    f_handler = logging.FileHandler(log_file)
    f_handler.setFormatter(formatter)
    logger.addHandler(f_handler)

    return logger

def log_event(logger: logging.Logger, message: str, level: str = 'info'):
    """Helper to dispatch log messages based on level."""
    levels = {
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'debug': logger.debug
    }
    
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)

if __name__ == '__main__':
    log = setup_logger('autoclicker_core')
    log_event(log, 'Logger initialization successful')