from exceptions import *

class HandleRequest:

    @classmethod
    def validate_send_bulk_message_payload(cls, payload):
        """
        Validates the payload for send_bulk_message.
        Raises ValueError if any required fields are missing or invalid.
        """
        required_fields = ['integrated_number', 'content_type', 'payload']
        payload_required_fields = ["type", "template"]
        template_fields = ["name", "language", "to_and_components"]
        for field in required_fields:
            if field not in payload:
                raise InvalidPayloadError(f"Missing required field: {field}")
        for field in payload_required_fields:
            if field not in payload['payload']:
                raise InvalidPayloadError(f"Missing required field: {field}")
        for field in template_fields:
            if field not in payload['payload']['template']:
                raise InvalidPayloadError(f"Missing required field: {field}")

        # Additional validation for components
        for component in payload['payload']['template']['to_and_components']:
            if ("to" not in component) or ("components" not in component):
                raise InvalidPayloadError("Each to_and_component must include a 'to' and 'components' field.")

    @classmethod
    def validate_send_single_message_payload(cls, payload):
        """
        Validates the payload for send_bulk_message.
        Raises ValueError if any required fields are missing or invalid.
        """
        required_fields = ['integrated_number', 'content_type', 'payload']
        payload_required_fields = ["to", "type", "template"]
        template_fields = ["name", "language", "components"]
        for field in required_fields:
            if field not in payload:
                raise InvalidPayloadError(f"Missing required field: {field}")
        for field in payload_required_fields:
            if field not in payload['payload']:
                raise InvalidPayloadError(f"Missing required field: {field}")
        for field in template_fields:
            if field not in payload['payload']['template']:
                raise InvalidPayloadError(f"Missing required field: {field}")




