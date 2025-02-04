# Custom exceptions for the SDK
from utils import get_logger

logger = get_logger('msg91-whatsapp-SDK')

class WhatsappError(Exception):
    """Base Class, all module exceptions are inherited from this class"""

    def __init__(self, message=None):
        super().__init__(message or "An error occurred in the WhatsApp SDK")


class ServiceErrors(WhatsappError):
    """Base class for service errors"""

    def __init__(self, message=None, status_code=None):
        super().__init__(message or "A service error occurred")
        self.status_code = status_code or 500


class AuthError(ServiceErrors):
    def __init__(self, message=None, status_code=401):
        super().__init__(message or "Authentication failed", status_code)


class ResponseFailureError(ServiceErrors):
    def __init__(self, message=None, status_code=502):
        super().__init__(message or "Failed to process the response", status_code)


class TimeOutError(ServiceErrors):
    def __init__(self, message=None, status_code=408):
        super().__init__(message or "The request timed out", status_code)


class SessionExpiredError(ServiceErrors):
    def __init__(self, message=None, status_code=404):
        super().__init__(message or "Session has expired", status_code)


class InvalidPayloadError(ServiceErrors):
    def __init__(self, message=None, status_code=400):
        super().__init__(message or "Invalid payload parameters", status_code)


class InvalidResponseError(ServiceErrors):
    def __init__(self, message=None, status_code=400):
        super().__init__(message or "Invalid response received", status_code)
