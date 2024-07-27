
class HttpNotFound(Exception):
    def __init__(self, message: str, status_code: int = 404):
        super().__init__(message, status_code)
        self.message = message
        self.name = "Not Found"
        self.status_code = status_code
        
        