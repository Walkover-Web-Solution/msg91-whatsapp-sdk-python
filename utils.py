# Utility functions (e.g., logging, validation)
import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

)

def get_logger(name):
    """
    Returns a configured logger instance.
    :param name: Name of the logger (usually the module name).
    :return: Logger instance.
    """
    return logging.getLogger(name)

# Example validation utility
def validate_url(url):
    """
    Validates a given URL.
    :param url: The URL to validate.
    :return: True if valid, raises ValueError otherwise.
    """
    if not url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL format: URL must start with http:// or https://")
    return True
