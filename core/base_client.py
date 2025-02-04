# Base client for API interactions
from session import SDKSession


class BaseClient:
    def __init__(self, base_url, headers=None):
        self.session = SDKSession(base_url, headers)

    def _get(self, endpoint, params=None):
        return self.session.request("GET", params=params)

    def _post(self, data=None, json=None):
        return self.session.request("POST", data=data, json=json)

    def _put(self, data=None, json=None):
        return self.session.request("PUT", data=data, json=json)

    def _delete(self, data=None, json=None):
        return self.session.request("DELETE", data=data, json=json)
