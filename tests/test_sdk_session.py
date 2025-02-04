
import unittest

from requests import ReadTimeout

from session import SDKSession
from exceptions import ServiceErrors
from unittest.mock import patch, Mock

class TestSDKSession(unittest.TestCase):

    def setUp(self):
        self.base_url = "https://api.example.com"
        self.headers = {"Authorization": "Bearer test_token"}
        self.sdk_session = SDKSession(base_url=self.base_url, headers=self.headers)

    def tearDown(self):
        self.sdk_session.close()

    @patch("session.requests.Session.request")
    def test_get_request_success(self, mock_request):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "success"}
        mock_request.return_value = mock_response

        response = self.sdk_session.request("GET")
        self.assertEqual(response, {"message": "success"})
    
    @patch("session.requests.Session.request")
    def test_get_request_connection_error(self, mock_request):
        mock_request.side_effect = ConnectionError("Connection failed")

        with self.assertRaises(ServiceErrors) as context:
            self.sdk_session.request("GET")
        self.assertIn("Connection error occurred", str(context.exception))

    @patch("session.requests.Session.request")
    def test_get_request_timeout(self, mock_request):
        mock_request.side_effect = ReadTimeout("Request timed out")

        with self.assertRaises(ServiceErrors) as context:
            self.sdk_session.request("GET")
        self.assertIn("Request timed out", str(context.exception))

if __name__ == "__main__":
    unittest.main()
