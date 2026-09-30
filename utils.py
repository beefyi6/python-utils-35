import time
from typing import Dict, Any

class ValidationError(ValueError):
    """Exception raised for invalid autoclicker configurations."""
    pass

class ClickProcessor:
    """Handles input validation and simulated execution for the autoclicker."""
    
    VALID_BUTTONS = {"left", "right", "middle"}

    def __init__(self):
        self.running = False

    def validate_inputs(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validates execution configuration before running the click loop."""
        validated = {}
        
        # Validate interval limit (prevent division-by-zero or system freezes)
        interval = config.get("interval", 0.1)
        try:
            interval = float(interval)
        except (TypeError, ValueError):
            raise ValidationError("Interval must be a valid float value")
        if interval <= 0.001:
            raise ValidationError("Interval must be greater than 0.001 seconds")
        validated["interval"] = interval

        # Validate target mouse button
        button = str(config.get("button", "left")).lower()
        if button not in self.VALID_BUTTONS:
            raise ValidationError(f"Mouse button must be one of {self.VALID_BUTTONS}")
        validated["button"] = button

        # Validate click limits (0 means infinite clicking)
        clicks = config.get("clicks", 0)
        try:
            clicks = int(clicks)
        except (TypeError, ValueError):
            raise ValidationError("Clicks count must be a valid integer")
        if clicks < 0:
            raise ValidationError("Clicks count cannot be negative")
        validated["clicks"] = clicks

        return validated

    def execute_safely(self, raw_config: Dict[str, Any]) -> bool:
        """Runs validation and prepares the autoclicker execution loop."""
        try:
            clean_config = self.validate_inputs(raw_config)
            self.running = True
            # Simulated iteration using the validated values
            print(f"Safe config validated: {clean_config}")
            return True
        except ValidationError as error:
            print(f"Config rejected: {error}")
            self.running = False
            return False
