import random
import time
from typing import Tuple, List

def get_jittered_position(x: int, y: int, radius: int = 3) -> Tuple[int, int]:
    """Adds a slight random offset to coordinates to mimic human clicking."""
    if radius <= 0:
        return x, y
    dx = random.randint(-radius, radius)
    dy = random.randint(-radius, radius)
    return x + dx, y + dy

def humanized_sleep(target_delay: float, fluctuation: float = 0.15) -> None:
    """Suspends execution for a target duration with a human-like variation."""
    if target_delay <= 0:
        return
    min_delay = max(0.001, target_delay * (1.0 - fluctuation))
    max_delay = target_delay * (1.0 + fluctuation)
    actual_delay = random.uniform(min_delay, max_delay)
    time.sleep(actual_delay)

def parse_coordinate_list(raw_input: str) -> List[Tuple[int, int]]:
    """Parses a string of comma and semicolon separated coordinates."""
    coordinates = []
    if not raw_input:
        return coordinates

    pairs = raw_input.split(";")
    for pair in pairs:
        clean_pair = pair.strip()
        if not clean_pair:
            continue
        try:
            x_str, y_str = clean_pair.split(",")
            coordinates.append((int(x_str.strip()), int(y_str.strip())))
        except ValueError:
            continue
    return coordinates
