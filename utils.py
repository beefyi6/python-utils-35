import json
import os
from typing import Any, Dict, List


def validate_click_event(event: Dict[str, Any]) -> bool:
    """Validate single autoclicker event data structure."""
    required_keys = {"x", "y", "delay", "button"}
    if not required_keys.issubset(event.keys()):
        return False

    if not (isinstance(event["x"], int) and isinstance(event["y"], int)):
        return False

    if event["x"] < 0 or event["y"] < 0:
        return False

    if not isinstance(event["delay"], (int, float)) or event["delay"] < 0:
        return False

    valid_buttons = {"left", "right", "middle", "double"}
    if event["button"] not in valid_buttons:
        return False

    return True


def load_click_profile(filepath: str) -> List[Dict[str, Any]]:
    """Load and validate click sequences from a JSON profile file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Profile path does not exist: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Profile data must be a list of click events")

    for index, event in enumerate(data):
        if not isinstance(event, dict) or not validate_click_event(event):
            raise ValueError(f"Invalid event configuration at index {index}")

    return data


def save_click_profile(filepath: str, events: List[Dict[str, Any]]) -> bool:
    """Validate and export click sequence to JSON file."""
    for index, event in enumerate(events):
        if not validate_click_event(event):
            raise ValueError(f"Cannot save invalid event at index {index}")

    parent_dir = os.path.dirname(os.path.abspath(filepath))
    os.makedirs(parent_dir, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)

    return True
