# MSG91 WhatsApp SDK

## Overview
The MSG91 WhatsApp SDK is a Python package that simplifies interaction with the MSG91 WhatsApp API. This SDK provides tools for managing bulk messages, handling responses, and streamlining API requests, making it easier to integrate WhatsApp messaging into your Python applications.

## Features
- Send bulk messages with dynamic templates and components.
- Handle responses with robust validation.
- Manage API sessions with automatic retries.
- Simplify payload construction for complex templates.
- Built-in utilities for logging and payload validation.

## Installation
To install the SDK, use pip:

```bash
pip install msg91-whatsapp-SDK
```

## Getting Started

### 1. Initialize the SDK
Start by creating an instance of the `WhatsappOutbound` class:

```python
from services.outbound_service import WhatsappOutbound

outbound_session = WhatsappOutbound(token="your_access_token")
```

### 2. Send a Bulk Message
Use the `send_bulk_message` method to send a bulk message:

```python
payload = {
    "integrated_number": "917314848007",
    "content_type": "template",
    "payload": {
        "messaging_product": "whatsapp",
        "type": "template",
        "template": {
            "name": "link_tracking_test",
            "language": {
                "code": "en",
                "policy": "deterministic"
            },
            "namespace": "338cef55_a0f8_4b2e_97f4_e030a0b94927",
            "to_and_components": [
                {
                    "to": [
                        "919893340296"
                    ],
                    "components": {
                        "button_1": {
                            "subtype": "url",
                            "type": "text",
                            "value": "sfdsf"
                        }
                    }
                }
            ]
        }
    }
}

request_id = outbound_session.send_bulk_message(payload)
print(request_id)
```

### 3. Validate Bulk Response
You can validate the response using the `validate_bulk_response` method:

```python
from response_handler import validate_bulk_response

response = {
    "status": "success",
    "hasError": False,
    "data": "Your request is in process, check delivery reports for status",
    "errors": None,
    "request_id": "7dc9157ab37f4ab683e73d4f0a7c111a"
}

validate_bulk_response(response)
```

## Dependencies
- Python 3.6+
- `requests`

## Development
Clone the repository and install the dependencies:

```bash
git clone https://github.com/yourusername/msg91-whatsapp-SDK.git
cd msg91-whatsapp-SDK
pip install -r requirements.txt
```

## Testing
Run the test suite using `unittest`:

```bash
python -m unittest discover tests
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

For more information, visit [MSG91 WhatsApp API Documentation](https://msg91.com).

