# Common logic for handling API responses
from exceptions import *

class HandleResponse:
    @classmethod
    def validate_bulk_response(cls, **kwargs):
        """
        Validates the response for bulk message requests.
        Raises ValueError if any required fields are missing or invalid.
        """
        try:
            required_fields = ["status", "hasError", "data", "request_id"]
            for field in required_fields:
                if field not in kwargs:
                    raise KeyError(f"Missing required field in response: {field}")
            if kwargs["status"] != "success":
                raise ResponseFailureError(f"Unexpected status: {kwargs['status']}")
        except KeyError as e:
            raise InvalidResponseError("Response status is missing")
        except Exception as e:
            raise e

    @classmethod
    def validate_single_response(cls, **kwargs):
        """
        Validates the response for single message requests.
        Raises ValueError if any required fields are missing or invalid.
        """
        try:
            required_fields = ["status", "hasError", "data", "request_id"]
            for field in required_fields:
                if field not in kwargs:
                    raise KeyError(f"Missing required field in response: {field}")
            if kwargs["status"] != "success":
                raise ResponseFailureError(f"Unexpected status: {kwargs['status']}")
        except KeyError as e:
            raise InvalidResponseError("Response status is missing")
        except Exception as e:
            raise e

