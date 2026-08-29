import time

def main_processing_loop():
    """Main loop for handling autoclicker inputs with validation"""
    click_count = 0
    print("Autoclicker handler initialized")
    while True:
        user_input = input("Enter clicks (or 'quit' to stop): ").strip().lower()
        if user_input == "quit":
            print("Exiting main loop")
            break
        # Input validation
        try:
            num_clicks = int(user_input)
            if num_clicks < 1 or num_clicks > 1000:
                print("Error: Clicks must be between 1 and 1000")
                continue
        except ValueError:
            print("Error: Please enter a valid integer")
            continue
        # Get interval with validation
        interval_input = input("Enter interval seconds (0.1 to 10): ").strip()
        try:
            interval = float(interval_input)
            if interval < 0.1 or interval > 10:
                print("Error: Interval must be between 0.1 and 10")
                continue
        except ValueError:
            print("Error: Please enter a valid number for interval")
            continue
        # Now the processing part of the loop
        print(f"Processing {num_clicks} clicks at {interval}s interval")
        for i in range(num_clicks):
            # Simulate autoclick
            print(f"  Click {i + 1} executed")
            time.sleep(interval)
        click_count += num_clicks
        print(f"Total clicks so far: {click_count}")

if __name__ == "__main__":
    main_processing_loop()