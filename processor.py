import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_clicks(interval, iterations):
    """Executes clicks based on validated user input."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be a positive number greater than 0.01s")
    
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError("Iterations must be an integer greater than 0")

    logger.info(f"Starting autoclicker: {iterations} clicks at {interval}s interval")
    
    for i in range(iterations):
        try:
            # Simulated click operation
            print(f"Performing click {i + 1}/{iterations}")
            time.sleep(interval)
        except KeyboardInterrupt:
            logger.warning("Processing interrupted by user")
            break

def main():
    # Example loop with validation logic
    user_input = {'interval': 0.5, 'count': 5}
    
    try:
        process_clicks(user_input['interval'], user_input['count'])
    except (ValueError, KeyError) as e:
        logger.error(f"Invalid configuration detected: {e}")

if __name__ == "__main__":
    main()