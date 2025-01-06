# Jwt Authentication handling
class AuthHandler:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {"Authorization": f"Bearer {self.token}"}
