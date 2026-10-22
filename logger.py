import logging
import sys

def setup_logger(name: str = "autoclicker") -> logging.Logger:
    """Configures and returns a standard application logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Output to stdout for easier container/cli monitoring
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# Global logger instance for the project
app_logger = setup_logger()