import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(
    name: str = "autoclicker",
    log_file: str = "logs/autoclicker.log",
    level: int = logging.INFO,
    max_bytes: int = 1_048_576,
    backup_count: int = 5,
    log_to_console: bool = True,
) -> logging.Logger:
    """Configures and returns a logger with rotating file handler."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers when re-initializing logger
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    file_handler = RotatingFileHandler(
        filename=log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)

    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(level)
        logger.addHandler(console_handler)

    return logger


def log_click_action(logger: logging.Logger, x: int, y: int, button: str = "left") -> None:
    """Log details about a mouse click event in the autoclicker."""
    logger.debug(f"Mouse click performed: button={button}, position=({x}, {y})")


def log_interval_change(logger: logging.Logger, new_interval: float) -> None:
    """Log changes to the autoclicker interval timer."""
    logger.info(f"Click interval updated to {new_interval:.3f} seconds")
