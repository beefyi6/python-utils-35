import time
import threading
import pyautogui

class ClickProcessor:
    def __init__(self, interval=0.01):
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def start_clicking(self):
        """Executes clicks using high-performance polling loop."""
        self.running = True
        # Use local references for faster lookup in hot loop
        click = pyautogui.click
        sleep = time.sleep
        interval = self.interval

        while self.running:
            click()
            sleep(interval)

    def stop(self):
        with self._lock:
            self.running = False

    def update_frequency(self, new_interval):
        """Adjusts click rate dynamically without re-instantiation."""
        with self._lock:
            self.interval = max(0.001, new_interval)

def execute_task(iterations, delay=0.01):
    """Batch execution optimization for autoclicker tasks."""
    click = pyautogui.click
    sleep = time.sleep
    
    for _ in range(iterations):
        click()
        sleep(delay)

# Optimized constants for click handling
PRECISION_MODE = True
DEFAULT_LATENCY = 0.001