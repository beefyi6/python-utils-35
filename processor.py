import time
import logging

def run_click_loop(click_interval, max_clicks):
    """
    Executes the clicking logic with input validation.
    """
    if not isinstance(click_interval, (int, float)) or click_interval < 0.01:
        raise ValueError("Interval must be a number >= 0.01 seconds")
        
    if not isinstance(max_clicks, int) or max_clicks < 1:
        raise ValueError("Max clicks must be a positive integer")

    logging.info(f"Starting clicker: {max_clicks} clicks at {click_interval}s interval")
    
    try:
        for i in range(max_clicks):
            # Perform mouse click logic here
            time.sleep(click_interval)
            logging.debug(f"Click {i+1} performed")
    except KeyboardInterrupt:
        logging.info("Process interrupted by user")
    finally:
        logging.info("Clicking cycle completed")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # Example usage with validated parameters
    run_click_loop(0.5, 10)