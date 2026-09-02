import time
import random
from typing import Tuple, List

def randomize_coordinates(x: int, y: int, max_variance: int = 3) -> Tuple[int, int]:
    """Add small random offset to coordinates for more human-like behavior."""
    offset_x = random.randint(-max_variance, max_variance)
    offset_y = random.randint(-max_variance, max_variance)
    return x + offset_x, y + offset_y

def get_random_delay(min_delay: float = 0.05, max_delay: float = 0.5) -> float:
    """Return a random delay in seconds between min and max."""
    return random.uniform(min_delay, max_delay)

def apply_random_delay(min_delay: float = 0.05, max_delay: float = 0.5) -> None:
    """Pause execution for a random duration."""
    delay = get_random_delay(min_delay, max_delay)
    time.sleep(delay)

def validate_position(x: int, y: int, width: int, height: int) -> bool:
    """Check if the position is within the given screen dimensions."""
    return 0 <= x <= width and 0 <= y <= height

def generate_click_positions(base_x: int, base_y: int, count: int, variance: int = 5) -> List[Tuple[int, int]]:
    """Generate a list of slightly varied positions around a base point."""
    positions = []
    for _ in range(count):
        pos = randomize_coordinates(base_x, base_y, variance)
        positions.append(pos)
    return positions

def calculate_interval(min_interval: float, max_interval: float, human_factor: float = 0.1) -> float:
    """Calculate click interval with some randomness for human simulation."""
    base = random.uniform(min_interval, max_interval)
    variation = random.uniform(-human_factor, human_factor)
    return max(0.01, base + variation)

def safe_click_duration() -> float:
    """Return a short random duration for button press in seconds."""
    return random.uniform(0.01, 0.1)
