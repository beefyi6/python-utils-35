import json
from typing import Any, Dict, List


def load_json(file_path: str) -> Dict[str, Any]:
    """Load JSON data from a given file path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading JSON: {e}")


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """Save JSON data to a given file path."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except IOError as e:
        raise ValueError(f"Error saving JSON: {e}")


def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Filter a list of dictionaries based on a key-value pair."""
    return [item for item in data if item.get(key) == value]


def merge_data(data1: Dict[str, Any], data2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries, with data2 overwriting data1 on conflicts."""
    merged = data1.copy()
    merged.update(data2)
    return merged
