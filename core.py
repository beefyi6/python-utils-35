from typing import List, Dict, Any


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Processes a list of data dictionaries by applying transformations.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries to process.

    Returns:
        List[Dict[str, Any]]: A list of processed dictionaries.
    """
    processed_data = []
    for item in data:
        transformed_item = {key: str(value).upper() for key, value in item.items()}
        processed_data.append(transformed_item)
    return processed_data


def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """
    Filters a list of data dictionaries based on a key-value pair.

    Args:
        data (List[Dict[str, Any]]): A list of dictionaries to filter.
        key (str): The key to check in each dictionary.
        value (Any): The value to match against.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries matching the key-value criteria.
    """
    return [item for item in data if item.get(key) == value]


def main():
    example_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
    ]
    processed = process_data(example_data)
    filtered = filter_data(processed, 'AGE', '25')
    print(filtered)


if __name__ == '__main__':
    main()