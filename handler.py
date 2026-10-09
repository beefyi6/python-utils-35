import json
import os
from typing import List, Dict, Any

class ClickSequenceHandler:
    """Handles serialization, deserialization, and validation of autoclicker sequences."""

    @staticmethod
    def validate_step(step: Dict[str, Any]) -> bool:
        """Validates a single autoclicker step."""
        required_keys = {"x", "y", "delay", "button"}
        if not all(key in step for key in required_keys):
            return False
        if not (isinstance(step["x"], (int, float)) and isinstance(step["y"], (int, float))):
            return False
        if not isinstance(step["delay"], (int, float)) or step["delay"] < 0:
            return False
        if step["button"] not in {"left", "right", "middle"}:
            return False
        return True

    @classmethod
    def load_sequence(cls, filepath: str) -> List[Dict[str, Any]]:
        """Loads and validates a click sequence from a JSON file."""
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Sequence file not found: {filepath}")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Sequence data must be a JSON list of click steps")

        for index, step in enumerate(data):
            if not cls.validate_step(step):
                raise ValueError(f"Invalid sequence format at index {index}: {step}")

        return data

    @classmethod
    def save_sequence(cls, filepath: str, sequence: List[Dict[str, Any]]) -> None:
        """Validates and saves a click sequence to a JSON file."""
        for index, step in enumerate(sequence):
            if not cls.validate_step(step):
                raise ValueError(f"Invalid step detected at index {index}: {step}")

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(sequence, f, indent=4)

    @staticmethod
    def calculate_total_duration(sequence: List[Dict[str, Any]]) -> float:
        """Calculates the total duration of the click sequence in seconds."""
        return sum(step.get("delay", 0.0) for step in sequence)
