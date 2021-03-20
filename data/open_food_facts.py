import requests
from config import FROM_PAGE, TO_PAGE, PAGE_SIZE, URL

class OFF_requests:
    def __init__(self):
        self.url = URL
        self.params = {"action": "process", "page_size": PAGE_SIZE, "json": "true"}

    def collect_data(self) -> list:
        """Collect result from api request."""
        data = {}
        for page in range(FROM_PAGE, TO_PAGE + 1) :
            self.params['page'] = page
            r = requests.get(self.url, self.params)
            if r.status_code == requests.codes.ok:
                data[page] = r.json()    
            else:
                r.raise_for_status()
        return data
