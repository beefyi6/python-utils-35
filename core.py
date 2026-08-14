import time
import requests
from requests.exceptions import RequestException

class NetworkOperation:
    MAX_RETRIES = 3
    RETRY_DELAY = 2  # seconds

    @staticmethod
    def fetch_data(url):
        attempt = 0
        while attempt < NetworkOperation.MAX_RETRIES:
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raises HTTPError for bad responses
                return response.json()  # Return JSON content
            except RequestException as e:
                attempt += 1
                print(f"Attempt {attempt} failed: {e}")
                if attempt < NetworkOperation.MAX_RETRIES:
                    time.sleep(NetworkOperation.RETRY_DELAY)
                else:
                    print("Max retries reached. Exiting.")
                    return None

# Example usage
if __name__ == '__main__':
    url = 'https://api.example.com/data'
    data = NetworkOperation.fetch_data(url)
    if data:
        print(data)
    else:
        print("Failed to retrieve data.")