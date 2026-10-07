import time
import pyautogui

def validate_interval(interval):
    """Ensures click interval is a positive float."""
    try:
        val = float(interval)
        if val <= 0:
            raise ValueError("Interval must be greater than zero.")
        return val
    except (ValueError, TypeError):
        return None

def run_autoclicker(interval, duration):
    """
    Main processing loop with input validation.
    Executes clicks based on validated parameters.
    """
    valid_interval = validate_interval(interval)
    if valid_interval is None:
        print("Invalid interval provided. Aborting.")
        return

    if not isinstance(duration, (int, float)) or duration <= 0:
        print("Invalid duration provided. Aborting.")
        return

    print(f"Starting autoclicker: {valid_interval}s interval for {duration}s.")
    end_time = time.time() + duration
    
    try:
        while time.time() < end_time:
            pyautogui.click()
            time.sleep(valid_interval)
    except KeyboardInterrupt:
        print("Execution stopped by user.")

if __name__ == '__main__':
    # Example usage for process simulation
    run_autoclicker(0.5, 5.0)