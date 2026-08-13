import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming JSON response is expected
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            raise NetworkError(f"Failed to get a successful response: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay)  # Wait before retrying
            else:
                raise NetworkError(f"Max retries exceeded for {url}")
    return None

# Example usage:
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(f"Network operation failed: {e}")
