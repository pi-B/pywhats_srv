class PyWhatsException(Exception):
    
    def __init__(self, error_format: str):
        self.format = error_format
        super().__init__(self.format)