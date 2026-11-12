import logging
import json
from datetime import datetime
from pathlib import Path

LOG_FILE = "autoclicker_data.jsonl"

# Configure logger for system events
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

def log_click_event(x: int, y: int, button: str) -> None:
    """
    Append click coordinates and metadata to local log file.
    """
    event_data = {
        "timestamp": datetime.now().isoformat(),
        "x": x,
        "y": y,
        "button": button
    }
    
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(event_data) + "\n")
    except IOError as e:
        logging.error(f"failed to write event to disk: {e}")

def get_event_history(limit: int = 100) -> list:
    """
    Retrieve recent click events from the storage file.
    """
    path = Path(LOG_FILE)
    if not path.exists():
        return []
        
    history = []
    try:
        with open(path, "r") as f:
            lines = f.readlines()[-limit:]
            for line in lines:
                history.append(json.loads(line))
    except (IOError, json.JSONDecodeError) as e:
        logging.error(f"failed to parse history file: {e}")
        
    return history