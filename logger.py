import logging
import sys
from pathlib import Path
from typing import Union


class SafeClickLogger:
    """Configures resilient logging for autoclicker events with fallback handlers."""

    def __init__(self, log_dir: Union[str, Path] = "logs", log_file: str = "clicker.log"):
        self.log_dir = Path(log_dir)
        self.log_filepath = self.log_dir / log_file
        self.logger = logging.getLogger("AutoClicker")
        self._configure_logging()

    def _configure_logging(self) -> None:
        """Initializes log handlers with error handling for file system edge cases."""
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "[%(asctime)s] %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Standard stdout handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Handle potential permission errors or invalid path issues when writing logs
        try:
            self.log_dir.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(self.log_filepath, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except (PermissionError, OSError) as err:
            self.logger.warning(
                f"File logging setup failed for '{self.log_filepath}': {err}. "
                "Continuing with console logging only."
            )

    def log_click(self, x: int, y: int, button: str = "left") -> None:
        """Logs click coordinates with validation for invalid inputs."""
        if not (isinstance(x, int) and isinstance(y, int)):
            self.logger.error(f"Invalid click coordinates encountered: x={x}, y={y}")
            return
        if x < 0 or y < 0:
            self.logger.warning(f"Out of bounds coordinate logged: ({x}, {y})")
            
        self.logger.info(f"Click executed at ({x}, {y}) using '{button}' button")

    def log_exception(self, context: str, error: Exception) -> None:
        """Safely logs unexpected runtime exceptions during execution loop."""
        err_msg = str(error) if str(error) else repr(error)
        self.logger.error(f"Execution failure in [{context}]: {err_msg}")
