import sys

# Configuration constants for autoclicker
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0
DEFAULT_BUTTON = 'left'
ALLOWED_BUTTONS = ['left', 'right', 'middle']

def validate_inputs(interval, button):
    """
    Validates processing parameters against defined constraints.
    """
    if not isinstance(interval, (int, float)):
        raise ValueError(f"Interval must be numeric, got {type(interval).__name__}")
    
    if not (MIN_INTERVAL <= interval <= MAX_INTERVAL):
        raise ValueError(f"Interval out of bounds: {interval}")
    
    if button not in ALLOWED_BUTTONS:
        raise ValueError(f"Invalid button: {button}. Use {ALLOWED_BUTTONS}")

def run_processing_loop(click_count, interval, button):
    """
    Main processing loop with parameter validation.
    """
    try:
        validate_inputs(interval, button)
        for i in range(click_count):
            print(f"Clicking {button} button at {interval}s interval")
    except ValueError as e:
        print(f"Validation error in processing loop: {e}", file=sys.stderr)
        sys.exit(1)