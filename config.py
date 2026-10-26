import os
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    """Global configuration for the autoclicker."""
    click_interval: float = 0.1
    button_code: str = 'left'
    default_hotkey: str = 'f8'
    log_path: str = "logs/app.log"

def get_config() -> AppConfig:
    """Initializes settings from environment variables with defaults."""
    return AppConfig(
        click_interval=float(os.getenv("CLICK_INTERVAL", 0.1)),
        button_code=os.getenv("BUTTON_CODE", "left"),
        default_hotkey=os.getenv("HOTKEY", "f8"),
        log_path=os.getenv("LOG_PATH", "logs/app.log")
    )

# Instantiate shared configuration instance
settings = get_config()