import time
import threading

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def _click_loop(self):
        while self.running:
            self.perform_click()
            time.sleep(self.interval)

    def perform_click(self):
        # Simulate a mouse click
        print('Mouse clicked!')  # Placeholder for actual click action

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.05)
    clicker.start()  # Start autoclicking
    time.sleep(1)  # Run for 1 second
    clicker.stop()  # Stop autoclicking
