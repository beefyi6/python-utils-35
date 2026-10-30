import json
import time
from typing import List, Dict, Any

class ClickDataProcessor:
    """Processes and formats autoclicker click sequences for execution and storage."""

    def __init__(self, default_delay: float = 0.1):
        self.default_delay = max(0.001, default_delay)

    def sanitize_click_event(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Normalizes raw click event data with default values and bounds checking."""
        x = int(event.get('x', 0))
        y = int(event.get('y', 0))
        button = str(event.get('button', 'left')).lower()
        if button not in ('left', 'right', 'middle'):
            button = 'left'

        delay = float(event.get('delay', self.default_delay))
        delay = max(0.001, min(delay, 3600.0))

        clicks = int(event.get('clicks', 1))
        clicks = max(1, min(clicks, 100))

        return {
            'x': max(0, x),
            'y': max(0, y),
            'button': button,
            'delay': delay,
            'clicks': clicks,
            'timestamp': float(event.get('timestamp', time.time()))
        }

    def process_sequence(self, raw_events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Processes a list of click events, sanitizing each entry."""
        processed = []
        for event in raw_events:
            if isinstance(event, dict):
                processed.append(self.sanitize_click_event(event))
        return processed

    def export_to_json(self, events: List[Dict[str, Any]]) -> str:
        """Serializes sanitized click events into a formatted JSON string."""
        clean_events = self.process_sequence(events)
        payload = {
            'version': '1.0',
            'count': len(clean_events),
            'events': clean_events
        }
        return json.dumps(payload, indent=2)

    def import_from_json(self, json_data: str) -> List[Dict[str, Any]]:
        """Parses JSON data and returns validated click events."""
        try:
            data = json.loads(json_data)
            events = data.get('events', []) if isinstance(data, dict) else []
            return self.process_sequence(events)
        except (json.JSONDecodeError, TypeError):
            return []
