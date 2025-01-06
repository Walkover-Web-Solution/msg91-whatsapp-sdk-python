from . import WhatsappAPI


class WhatsappTemplate(WhatsappAPI):
    def __init__(self, token):
        super().__init__(token)

    def get_template_curl(self, payload):
        # verifying payload
        payload =
        self._post(payload)

    def get_template_curl_bulk(self, payload):
        # verifying payload
        self._post(payload)



