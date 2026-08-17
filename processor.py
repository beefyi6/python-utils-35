import time
import random

class AutoClicker:
    def __init__(self, click_interval, duration):
        self.click_interval = click_interval
        self.duration = duration

    def validate_input(self):
        if not isinstance(self.click_interval, (int, float)) or self.click_interval <= 0:
            raise ValueError('Click interval must be a positive number.')
        if not isinstance(self.duration, (int, float)) or self.duration <= 0:
            raise ValueError('Duration must be a positive number.')

    def start(self):
        self.validate_input()
        end_time = time.time() + self.duration
        while time.time() < end_time:
            self.click()
            time.sleep(self.click_interval)

    def click(self):
        # Simulating a mouse click
        print('Click!')

# Example usage
if __name__ == '__main__':
    try:
        clicker = AutoClicker(click_interval=0.5, duration=10)
        clicker.start()
    except ValueError as e:
        print(f'Input error: {e}')