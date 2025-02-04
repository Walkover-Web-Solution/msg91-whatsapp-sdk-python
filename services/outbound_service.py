from core.response_handler import HandleResponse
from . import WhatsappAPI
from core.request_handler import HandleRequest

class WhatsappOutbound(WhatsappAPI):
    def __init__(self, token, endpoint = '/whatsapp-outbound-message/bulk/'):
        super().__init__(token, endpoint)
        self.request_handler = HandleRequest()
        self.response_handler = HandleResponse()

    def send_bulk_message(self, payload):
        """
                Sends a bulk message request.
        """
        try:
            self.request_handler.validate_send_bulk_message_payload(payload)
            resp = self._post(json=payload)
            self.response_handler.validate_bulk_response(**resp)
            return resp['request_id']
        except Exception as e:
            raise e

    def send_single_message(self, payload):
        """
                Sends a single message request.
        """
        try:
            self.request_handler.validate_send_single_message_payload(payload)
            resp = self._post(json=payload)
            self.response_handler.validate_single_response(**resp)
            return resp['request_id']
        except Exception as e:
            raise e



