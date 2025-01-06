# Base client for API interactions
from session import SDKSession


class BaseClient:
    def __init__(self, base_url, headers=None):
        self.session = SDKSession(base_url, headers)

    def _get(self, endpoint, params=None):
        return self.session.request("GET", endpoint, params=params)

    def _post(self, endpoint, data=None, json=None):
        return self.session.request("POST", endpoint, data=data, json=json)

    def _put(self, endpoint, data=None, json=None):
        return self.session.request("PUT", endpoint, data=data, json=json)

    def _delete(self, endpoint, data=None, json=None):
        return self.session.request("DELETE", endpoint, data=data, json=json)
