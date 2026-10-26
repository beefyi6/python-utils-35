import time
import threading
from typing import Callable, Optional


class FastClickerEngine:
    """High-performance click engine optimized for minimal overhead during rapid firing."""

    def __init__(self, click_action: Callable[[], None], cps: float = 100.0) -> None:
        self.click_action = click_action
        self.cps = cps
        self._running = False
        self._thread: Optional[threading.Thread] = None
        self.total_clicks = 0

    def set_cps(self, cps: float) -> None:
        """Update clicks per second dynamically."""
        self.cps = max(0.1, min(cps, 1000.0))

    def _optimized_loop(self) -> None:
        """Busy-wait hybrid sleep loop to maintain accurate click intervals."""
        # Cache references locally to reduce attribute lookup overhead in hot loop
        action = self.click_action
        get_time = time.perf_counter
        sleep = time.sleep

        next_click = get_time()
        while self._running:
            now = get_time()
            if now >= next_click:
                action()
                self.total_clicks += 1
                interval = 1.0 / self.cps
                next_click = now + interval

            # Yield CPU execution if time until next click is significant
            remaining = next_click - get_time()
            if remaining > 0.002:
                sleep(remaining - 0.001)

    def start(self) -> None:
        """Start the optimized auto-clicking loop in a background thread."""
        if self._running:
            return
        self._running = True
        self._thread = threading.Thread(target=self._optimized_loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop execution and wait for thread termination."""
        self._running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
