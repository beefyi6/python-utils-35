from typing import Any, Dict, Tuple


class InputValidator:
    def __init__(self: 'InputValidator') -> None:
        pass

    def validate_click_position(self: 'InputValidator', position: Tuple[int, int]) -> bool:
        """
        Validates the click position.

        Args:
            position (Tuple[int, int]): The x and y coordinates of the position.

        Returns:
            bool: True if the position is valid, False otherwise.
        """
        x, y = position
        return 0 <= x <= 1920 and 0 <= y <= 1080

    def validate_click_interval(self: 'InputValidator', interval: float) -> bool:
        """
        Validates the click interval.

        Args:
            interval (float): The time interval between clicks in seconds.

        Returns:
            bool: True if the interval is valid, False otherwise.
        """
        return interval > 0

    def validate_hotkey(self: 'InputValidator', hotkey: str) -> bool:
        """
        Validates the format of a hotkey.

        Args:
            hotkey (str): The hotkey string to validate.

        Returns:
            bool: True if the hotkey is valid, False otherwise.
        """
        valid_keys = ['ctrl', 'alt', 'shift', 'space', 'enter']
        return all(key in valid_keys or len(key) == 1 for key in hotkey.split('+'))


def main() -> None:
    validator = InputValidator()
    print(validator.validate_click_position((100, 200)))  # True
    print(validator.validate_click_interval(0.5))          # True
    print(validator.validate_hotkey('ctrl+alt'))          # True


if __name__ == '__main__':
    main()