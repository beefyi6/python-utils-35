import time
import urllib.request
import urllib.error
import json
import logging

logger = logging.getLogger("autoclicker.core")

class RemoteConfigLoader:
    """Handles downloading and updating autoclicker macro configurations remotely."""

    def __init__(self, url: str, max_retries: int = 3, backoff_factor: float = 2.0):
        self.url = url
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def fetch_config(self) -> dict:
        """Fetches macro configuration JSON with exponential backoff on connection errors."""
        delay = 1.0
        for attempt in range(1, self.max_retries + 1):
            try:
                logger.info(f"Fetching remote profile (attempt {attempt}/{self.max_retries})")
                req = urllib.request.Request(self.url, headers={"User-Agent": "Autoclicker-Utils/1.0"})
                with urllib.request.urlopen(req, timeout=4) as response:
                    return json.loads(response.read().decode("utf-8"))
            except (urllib.error.URLError, urllib.error.HTTPError) as e:
                logger.warning(f"Connection attempt {attempt} failed: {e}")
            except json.JSONDecodeError as e:
                logger.error(f"Malformed JSON configuration: {e}")
                raise ValueError("Invalid configuration format received") from e

            if attempt < self.max_retries:
                logger.info(f"Waiting {delay:.1f}s before retry...")
                time.sleep(delay)
                delay *= self.backoff_factor

        raise ConnectionError(f"Could not retrieve configuration from {self.url} after {self.max_retries} attempts")
