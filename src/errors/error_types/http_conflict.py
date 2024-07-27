
class HttpConflictError(Exception):
    def __init__(self, message: str, status_code: int = 409):
        super().__init__(message, status_code)
        self.message = message
        self.name = "Conflict"
        self.status_code = status_code
        
        