# Services package initialization

from ..core.base_client import BaseClient

class WhatsappAPI(BaseClient):
    def __init__(self, token):
        base_url = "https://whatsapp.phone91.com"
        headers = {"Jwt": f"Bearer {token}"}
        super().__init__(base_url, headers)