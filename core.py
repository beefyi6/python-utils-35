import time
import threading
try:
    import pyautogui
except ImportError:
    pyautogui = None
class AutoClickerCore:
    def __init__(self, click_interval=0.1, click_button='left', click_count=None):
        self.click_interval = click_interval
        self.click_button = click_button
        self.click_count = click_count
        self.is_running = False
        self.click_thread = None
        self.clicks_performed = 0
    def start_clicking(self):
        if self.is_running:
            return
        self.is_running = True
        self.clicks_performed = 0
        self.click_thread = threading.Thread(target=self._perform_clicks, daemon=True)
        self.click_thread.start()
    def stop_clicking(self):
        self.is_running = False
        if self.click_thread and self.click_thread.is_alive():
            self.click_thread.join(timeout=1.0)
        self.click_thread = None
    def _perform_clicks(self):
        while self.is_running:
            if self.click_count is not None and self.clicks_performed >= self.click_count:
                self.stop_clicking()
                break
            if pyautogui is not None:
                pyautogui.click(button=self.click_button)
            else:
                print(f"Simulated {self.click_button} click #{self.clicks_performed + 1}")
            self.clicks_performed += 1
            time.sleep(self.click_interval)
    def update_settings(self, interval=None, button=None, count=None):
        if interval is not None:
            self.click_interval = max(0.01, interval)
        if button is not None and button in ['left', 'right', 'middle']:
            self.click_button = button
        if count is not None:
            self.click_count = count if count > 0 else None
    def get_status(self):
        return {
            'running': self.is_running,
            'clicks': self.clicks_performed,
            'interval': self.click_interval,
            'button': self.click_button
        }
def demonstrate():
    core = AutoClickerCore(click_interval=0.2, click_count=3)
    print("Starting autoclicker demo")
    core.start_clicking()
    time.sleep(1)
    status = core.get_status()
    print(f"Status: {status}")
    core.stop_clicking()
    print("Stopped")
if __name__ == "__main__":
    demonstrate()