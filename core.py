import pyautogui
import time
from typing import Optional

class AutoClicker:
    """Automates mouse clicking actions for repetitive tasks."""

    def __init__(self, interval: float = 0.1, button: str = 'left') -> None:
        self.interval: float = interval
        self.button: str = button
        self.is_running: bool = False

    def start_clicking(self, clicks: Optional[int] = None) -> None:
        """Initiates the clicking sequence until stopped or count reached."""
        self.is_running = True
        count: int = 0
        try:
            while self.is_running:
                pyautogui.click(button=self.button)
                time.sleep(self.interval)
                count += 1
                if clicks and count >= clicks:
                    break
        except KeyboardInterrupt:
            self.stop_clicking()

    def stop_clicking(self) -> None:
        """Gracefully halts the active clicking sequence."""
        self.is_running = False

    def set_interval(self, seconds: float) -> None:
        """Updates the delay between individual clicks."""
        if seconds < 0:
            raise ValueError("Interval must be a positive number.")
        self.interval = seconds

def main() -> None:
    """Entry point for basic autoclicker demonstration."""
    clicker: AutoClicker = AutoClicker(interval=0.5)
    print("Starting clicker. Press Ctrl+C to stop.")
    clicker.start_clicking()

if __name__ == "__main__":
    main()