import time
import urllib.request
import urllib.error
import json
import logging

logger = logging.getLogger("autoclicker.handler")

class NetworkHandler:
    """Handles network requests for autoclicker configurations and coordinates with retries."""

    def __init__(self, base_url: str, max_retries: int = 3, backoff_factor: float = 1.5):
        self.base_url = base_url.rstrip('/')
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def fetch_coordinates(self, endpoint: str) -> dict:
        """
        Fetches remote clicking path configurations using exponential backoff.
        Prevents transient network blips from stopping the autoclicker daemon.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        delay = 1.0

        for attempt in range(1, self.max_retries + 1):
            try:
                logger.info(f"Attempt {attempt}/{self.max_retries} fetching from: {url}")
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "Python-Autoclicker-Utils/3.5"}
                )
                with urllib.request.urlopen(req, timeout=5) as response:
                    if response.status == 200:
                        return json.loads(response.read().decode('utf-8'))
            except (urllib.error.URLError, urllib.error.HTTPError) as err:
                logger.warning(f"Attempt {attempt} failed: {err}")
                if attempt == self.max_retries:
                    logger.error("Network request failed after maximum retries.")
                    raise err
                
                time.sleep(delay)
                delay *= self.backoff_factor

        raise RuntimeError("Failed to resolve coordinates fetch operational state.")
