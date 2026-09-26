from typing import Dict, Any, Tuple

class AutoClickerConfig:
    """
    Configuration management for the autoclicker application.
    
    Handles validation and storage of click intervals, mouse buttons, 
    hotkeys, and randomization factors to mimic human behavior.
    """

    def __init__(
        self,
        delay: float = 0.1,
        button: str = "left",
        hotkey: str = "f8",
        random_interval: Tuple[float, float] = (0.01, 0.05)
    ) -> None:
        self.delay: float = delay
        self.button: str = button
        self.hotkey: str = hotkey
        self.random_interval: Tuple[float, float] = random_interval
        self.validate()

    def validate(self) -> None:
        """
        Validates configuration parameters to prevent errors during operation.
        
        Raises:
            ValueError: If delay is negative, hotkey is empty, or interval bounds are invalid.
        """
        if self.delay <= 0:
            raise ValueError("Delay must be a positive float representing seconds.")
        
        valid_buttons = {"left", "right", "middle"}
        if self.button.lower() not in valid_buttons:
            raise ValueError(f"Button must be one of {valid_buttons}")
        
        if not self.hotkey:
            raise ValueError("Hotkey toggle shortcut cannot be empty.")
        
        min_rand, max_rand = self.random_interval
        if min_rand < 0 or max_rand < 0:
            raise ValueError("Randomization interval boundaries must be non-negative.")
        if min_rand > max_rand:
            raise ValueError("Minimum random delay cannot exceed maximum random delay.")

    def to_dict(self) -> Dict[str, Any]:
        """
        Serializes the configuration settings into a dictionary format.
        
        Returns:
            Dict[str, Any]: Dictionary representing the current settings.
        """
        return {
            "delay": self.delay,
            "button": self.button,
            "hotkey": self.hotkey,
            "random_interval": list(self.random_interval)
        }