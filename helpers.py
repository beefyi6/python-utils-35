def validate_click_params(interval, count):
    """Ensures click settings are within operational bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be a number >= 0.01 seconds.")
    
    if not isinstance(count, int) or count < -1:
        raise ValueError("Count must be a positive integer or -1 for infinite.")
    
    return True

def sanitize_input(value, default):
    """Provides fallback mechanism for user input configuration."""
    try:
        parsed = float(value)
        return parsed if parsed > 0 else default
    except (ValueError, TypeError):
        return default

def get_loop_control(iteration, limit):
    """Checks exit condition for the processing loop."""
    if limit == -1:
        return True
    return iteration < limit