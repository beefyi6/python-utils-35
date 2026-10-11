import json
import datetime
from pathlib import Path
from typing import Dict, Any

LOG_FILE = Path("click_history.json")

def save_click_event(action_data: Dict[str, Any]) -> None:
    """Appends a single click event to the persistent storage file."""
    event = {
        "timestamp": datetime.datetime.now().isoformat(),
        **action_data
    }
    
    history = []
    if LOG_FILE.exists():
        try:
            with open(LOG_FILE, "r") as f:
                history = json.load(f)
        except (json.JSONDecodeError, IOError):
            history = []
    
    history.append(event)
    
    with open(LOG_FILE, "w") as f:
        json.dump(history, f, indent=4)

def get_recent_clicks(limit: int = 10) -> list:
    """Retrieves the last n logged click events."""
    if not LOG_FILE.exists():
        return []
    
    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
            return data[-limit:]
    except (json.JSONDecodeError, IOError):
        return []