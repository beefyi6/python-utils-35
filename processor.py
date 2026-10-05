import time
import pyautogui

def validate_interval(interval):
    """Ensures click interval is within safe bounds."""
    if not isinstance(interval, (int, float)):
        raise ValueError("Interval must be a number")
    if interval < 0.01:
        return 0.01
    if interval > 60:
        return 60.0
    return interval

def run_autoclicker(clicks, interval):
    """Main processing loop with input validation."""
    try:
        validated_interval = validate_interval(interval)
        count = int(clicks)
        
        if count <= 0:
            print("Invalid click count: must be positive")
            return

        print(f"Starting {count} clicks with {validated_interval}s interval")
        for _ in range(count):
            pyautogui.click()
            time.sleep(validated_interval)
            
    except ValueError as e:
        print(f"Input validation error: {e}")
    except Exception as e:
        print(f"Unexpected execution error: {e}")

if __name__ == '__main__':
    # Example usage with validated parameters
    run_autoclicker(5, 0.5)