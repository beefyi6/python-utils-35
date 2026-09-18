import random
from typing import Dict, List, Any


class ClickDataProcessor:
    """Processes and normalizes raw click event data for autoclicker execution."""

    def __init__(self, default_interval: float = 0.1, apply_jitter: bool = False):
        self.default_interval = default_interval
        self.apply_jitter = apply_jitter

    def process_sequence(self, raw_sequence: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Normalizes a list of raw click event dictionaries into a standardized format.
        Ensures coordinates are non-negative integers and delays are positive floats.
        """
        processed = []
        for idx, item in enumerate(raw_sequence):
            x = int(item.get('x', 0))
            y = int(item.get('y', 0))
            button = str(item.get('button', 'left')).lower()
            interval = float(item.get('interval', self.default_interval))

            # Apply humanization jitter if enabled (adds slight variance)
            if self.apply_jitter and interval > 0:
                jitter = random.uniform(-0.1, 0.1) * interval
                interval = max(0.01, interval + jitter)

            processed.append({
                'id': idx + 1,
                'x': max(0, x),
                'y': max(0, y),
                'button': button if button in ('left', 'right', 'middle') else 'left',
                'delay': round(interval, 4),
                'clicks': max(1, int(item.get('clicks', 1)))
            })
        return processed

    def calculate_total_duration(self, sequence: List[Dict[str, Any]]) -> float:
        """Calculates total estimated execution time of a click sequence."""
        return round(sum(item.get('delay', 0.0) for item in sequence), 4)
