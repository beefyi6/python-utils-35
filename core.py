import sys
import time
import threading
from typing import Optional

class AutoclickerCore:
    """Core execution engine for high-frequency clicking with precise timing."""
    
    def __init__(self, interval_seconds: float = 0.01):
        self.interval = interval_seconds
        self.active = False
        self._worker_thread: Optional[threading.Thread] = None
        self._is_windows = sys.platform == "win32"
        
        if self._is_windows:
            import ctypes
            self._mouse_event = ctypes.windll.user32.mouse_event
        else:
            self._mouse_event = None

    def _trigger_click(self) -> None:
        """Executes raw mouse events using the fastest OS API available."""
        if self._is_windows and self._mouse_event:
            # MOUSEEVENTF_LEFTDOWN = 0x0002, MOUSEEVENTF_LEFTUP = 0x0004
            self._mouse_event(0x0002, 0, 0, 0, 0)
            self._mouse_event(0x0004, 0, 0, 0, 0)
        else:
            # Fallback execution simulation
            pass

    def _precise_loop(self) -> None:
        """Precision timing loop balancing CPU overhead and clock drift."""
        target_time = time.perf_counter()
        while self.active:
            current_time = time.perf_counter()
            if current_time >= target_time:
                self._trigger_click()
                target_time = current_time + self.interval
            
            # Hybrid sleep strategy to save CPU without losing precision
            time_remaining = target_time - time.perf_counter()
            if time_remaining > 0.01:
                time.sleep(time_remaining * 0.9)
            elif time_remaining > 0.001:
                time.sleep(0.001)
            else:
                # Yield control to prevent thread starvation
                time.sleep(0)

    def start(self) -> None:
        """Launches the click loop inside a separate background thread."""
        if not self.active:
            self.active = True
            self._worker_thread = threading.Thread(target=self._precise_loop, daemon=True)
            self._worker_thread.start()

    def stop(self) -> None:
        """Signals the click loop to terminate immediately."""
        self.active = False
        if self._worker_thread:
            self._worker_thread.join(timeout=1.0)
            self._worker_thread = None