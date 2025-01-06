# Wrapper for managing a persistent requests session

import requests

class SDKSession:
    def __init__(self, base_url, headers=None):
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.base_url = base_url

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
