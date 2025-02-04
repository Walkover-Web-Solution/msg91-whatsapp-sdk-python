# Services package initialization

from core.base_client import BaseClient

class WhatsappAPI(BaseClient):
    def __init__(self, token, endpoint):
        base_url = "https://testwhatsapp.phone91.com" + endpoint
        headers = {"Jwt": token}
        super().__init__(base_url, headers)