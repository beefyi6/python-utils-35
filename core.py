import time
import pyautogui

def run_autoclicker(interval, count):
    """Execute clicking loop with input validation."""
    try:
        if not isinstance(interval, (int, float)) or interval < 0.1:
            raise ValueError("Interval must be a float >= 0.1 seconds")
        if not isinstance(count, int) or count < 0:
            raise ValueError("Count must be a positive integer")
    except ValueError as e:
        print(f"Validation error: {e}")
        return

    print(f"Starting autoclicker: {count} clicks at {interval}s interval")
    
    for i in range(count):
        pyautogui.click()
        time.sleep(interval)
        print(f"Click {i + 1}/{count} performed")

def main():
    # Configuration settings
    click_interval = 1.0
    click_count = 5

    # Execution with validated inputs
    run_autoclicker(click_interval, click_count)

if __name__ == '__main__':
    main()