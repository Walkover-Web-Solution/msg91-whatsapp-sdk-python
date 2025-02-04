import requests
from http.client import RemoteDisconnected
from requests.exceptions import ReadTimeout, ConnectionError, HTTPError
from exceptions import ServiceErrors
from utils import get_logger

logger = get_logger('msg91-whatsapp-SDK')

class SDKSession:
    def __init__(self, base_url, headers=None, timeout=10):
        """
        Initializes the SDKSession with a base URL and optional headers.
        :param base_url: The base URL for the API.
        :param headers: Optional headers to include in every request.
        :param timeout: Default timeout for requests in seconds.
        """
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.base_url = base_url.rstrip('/')
        self._timeout = timeout

    def request(self, method, **kwargs):
        """
        Sends an HTTP request.
        :param method: HTTP method (GET, POST, etc.).
        :param kwargs: Additional arguments for the requests method.
        :return: Response JSON or raw response in case of non-JSON content.
        """
        url = self.base_url
        kwargs.setdefault('timeout', self._timeout)

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            
            # Attempt to parse JSON response
            try:
                return response.json()
            except ValueError:
                return response.text

        except (RemoteDisconnected, ConnectionError) as conn_err:
            self._log_error("Connection error", conn_err)
            raise ServiceErrors(message="Connection error occurred", status_code=503)

        except ReadTimeout as timeout_err:
            self._log_error("Request timed out", timeout_err)
            raise ServiceErrors(message="Request timed out", status_code=408)

        except HTTPError as http_err:
            self._log_error("HTTP error", http_err)
            raise ServiceErrors(message=f"HTTP error: {http_err}", status_code=response.status_code)

        except Exception as generic_err:
            self._log_error("Unexpected error", generic_err)
            raise ServiceErrors(message="An unexpected error occurred", status_code=500)

    def close(self):
        """
        Closes the session.
        """
        self.session.close()

    @staticmethod
    def _log_error(message, error):
        """
        Logs error details (extend this for real logging).
        :param message: Custom error message.
        :param error: The exception object.
        """
        logger.error(f"[ERROR] {message}: {str(error)}")
