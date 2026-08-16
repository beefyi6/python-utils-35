import time
from typing import Optional

class AutoClicker:
    def __init__(self, interval: float, duration: Optional[float] = None) -> None:
        """
        Initializes the AutoClicker with a specific interval and optional duration.
        
        :param interval: The time interval (in seconds) between clicks.
        :param duration: The total duration (in seconds) to run the auto clicker. If None, runs indefinitely.
        """
        self.interval = interval
        self.duration = duration
        self.start_time = time.time() if duration is not None else None

    def click(self) -> None:
        """
        Simulates a mouse click. This should be replaced with actual click functionality.
        """
        print("Click!")  # Placeholder for the actual click action

    def run(self) -> None:
        """
        Starts the auto clicker, executing clicks at the specified interval for the specified duration.
        """
        while True:
            self.click()
            if self.duration is not None:
                elapsed = time.time() - self.start_time
                if elapsed >= self.duration:
                    break
            time.sleep(self.interval)
