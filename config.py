import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def configure_logger(
    name: str = "autoclicker",
    log_dir: str = "logs",
    log_file: str = "app.log",
    max_size_mb: int = 10,
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """Set up logger with rotation for autoclicker logs."""
    # Create log directory if it does not exist
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    full_log_path = log_path / log_file
    # Get or create the logger instance
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # Clear existing handlers to avoid duplicates on reconfig
    if logger.hasHandlers():
        logger.handlers.clear()
    # Set up rotating file handler
    max_bytes = max_size_mb * 1024 * 1024
    file_handler = RotatingFileHandler(
        full_log_path,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8"
    )
    file_handler.setLevel(level)
    # Set up console handler for immediate output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    # Define consistent log format
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # Attach handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

# Demonstrate usage when run directly
if __name__ == "__main__":
    logger = configure_logger(level=logging.DEBUG)
    logger.info("Autoclicker application initialized")
    logger.debug("Detailed debug information for testing")
    logger.warning("Warning about potential click delay")
    logger.error("Error occurred during automation")