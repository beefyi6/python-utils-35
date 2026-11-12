import time
from typing import Dict, Any, List, Optional


class ClickTaskHandler:
    """Handles and validates autoclicker command queues prior to execution."""

    VALID_CLICK_TYPES = {"left", "right", "middle", "double"}

    def __init__(self, tasks: List[Dict[str, Any]]):
        self.tasks = tasks
        self.processed_count = 0
        self.failed_count = 0

    def validate_task(self, task: Dict[str, Any]) -> bool:
        """Validates individual click parameters for correct types and ranges."""
        if not isinstance(task, dict):
            return False

        interval = task.get("interval", 0.1)
        click_type = task.get("click_type", "left")
        repeat_count = task.get("repeat_count", 1)
        coords = task.get("coords")

        if not isinstance(interval, (int, float)) or interval <= 0:
            return False

        if click_type not in self.VALID_CLICK_TYPES:
            return False

        if not isinstance(repeat_count, int) or repeat_count < 1:
            return False

        if coords is not None:
            if not isinstance(coords, (tuple, list)) or len(coords) != 2:
                return False
            if not all(isinstance(c, int) and c >= 0 for c in coords):
                return False

        return True

    def process_loop(self) -> int:
        """Main task execution loop with strict input validation."""
        for index, task in enumerate(self.tasks):
            if not self.validate_task(task):
                self.failed_count += 1
                print(f"[Error] Invalid task configuration skipped at index {index}")
                continue

            # Execute validated autoclicker command
            click_type = task.get("click_type", "left")
            repeat = task.get("repeat_count", 1)
            interval = task.get("interval", 0.1)
            coords = task.get("coords", "current position")

            print(f"[Processing] Type: {click_type} | Count: {repeat} | Interval: {interval}s | Coords: {coords}")
            self.processed_count += 1

        return self.processed_count
