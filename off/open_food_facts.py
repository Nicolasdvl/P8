"""
API requests.

Collect data from OpenFoodFacts API.
For more information : https://wiki.openfoodfacts.org/API
"""
import requests
from .config import FROM_PAGE, TO_PAGE, PAGE_SIZE, URL
from progress.bar import ChargingBar


class OFF_requests:
    """Contain request to OpenFoodFacts API."""

    def __init__(self):
        """Define request's params."""
        self.url = URL
        self.params = {
            "action": "process",
            "page_size": PAGE_SIZE,
            "json": "true",
        }

    def collect_data(self) -> dict:
        """Collect result from api request."""
        data = {}
        bar = ChargingBar("Récupération des données...", max=TO_PAGE)
        for page in range(FROM_PAGE, TO_PAGE + 1):
            self.params["page"] = page
            r = requests.get(self.url, self.params)
            if r.status_code == requests.codes.ok:
                data[page] = r.json()
            else:
                r.raise_for_status()
            bar.next()
        bar.finish()
        return data
