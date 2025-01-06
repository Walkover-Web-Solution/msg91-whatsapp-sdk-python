from . import WhatsappAPI


class WhatsappOutbound(WhatsappAPI):
    def __init__(self, token):
        super().__init__(token)

    def send_single_message(self, integrated_number, template_name, template_language, ):

        self._post(payload)

    def send_bulk_message(self, ):
        self._post(payload)



