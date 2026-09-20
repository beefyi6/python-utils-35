import logging
import sys
from datetime import datetime

def get_logger(name: str) -> logging.Logger:
    """Configures a standard logger for the autoclicker."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        log_filename = f"autoclicker_{datetime.now().strftime('%Y-%m-%d')}.log"
        file_handler = logging.FileHandler(log_filename)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def log_event(logger: logging.Logger, message: str, level: str = "info"):
    """Helper to route messages to appropriate log levels."""
    levels = {
        "info": logger.info,
        "warning": logger.warning,
        "error": logger.error,
        "debug": logger.debug
    }
    
    log_func = levels.get(level.lower(), logger.info)
    log_func(message)