import time
import logging

# Configure logging for the autoclicker process
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('handler')

def validate_inputs(clicks, interval):
    """Ensures click count and intervals are within operational bounds."""
    if not isinstance(clicks, int) or clicks <= 0:
        raise ValueError(f"Invalid click count: {clicks}. Must be positive integer.")
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError(f"Invalid interval: {interval}. Minimum is 0.01s.")
    return True

def run_click_loop(clicks, interval):
    """Executes the main autoclicker processing loop with validation."""
    try:
        validate_inputs(clicks, interval)
        logger.info(f"Starting sequence: {clicks} clicks at {interval}s interval")
        
        for i in range(clicks):
            # Simulate mouse event injection
            logger.debug(f"Click iteration {i+1} performed")
            time.sleep(interval)
            
        logger.info("Sequence completed successfully")
    except ValueError as e:
        logger.error(f"Validation error in processing loop: {e}")
    except Exception as e:
        logger.critical(f"Unexpected system failure: {e}")

if __name__ == "__main__":
    # Example usage for development testing
    run_click_loop(5, 0.5)