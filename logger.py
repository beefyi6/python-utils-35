import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(
    name: str = "autoclicker",
    log_file: str = "logs/autoclicker.log",
    max_bytes: int = 2 * 1024 * 1024,  # 2 MB
    backup_count: int = 5,
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configures and returns a logger with both console and rotating file handlers.
    Prevents duplicate handler registrations on repeated calls.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding handlers multiple times if logger is already configured
    if logger.handlers:
        return logger

    # Ensure target directory for logs exists
    log_path = Path(log_file)
    if log_path.parent:
        log_path.parent.mkdir(parents=True, exist_ok=True)

    # Define log message format
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console output handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Rotating file handler for persistent execution logs
    try:
        file_handler = RotatingFileHandler(
            filename=log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)
    except (OSError, PermissionError) as err:
        logger.warning(f"File logging disabled, unable to write to {log_file}: {err}")

    return logger