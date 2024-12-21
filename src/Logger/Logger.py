import logging

class Logger:
    def __init__(self, name: str, log_file: str = "app.log"):
        # logger creation
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Add handlers..
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def log(self, message: str, request_id: str = None):
        if request_id:
            message = f"[Request ID: {request_id}] {message}"
        self.logger.info(message)

    def log_error(self, message: str, request_id: str = None):
        if request_id:
            message = f"[Request ID: {request_id}] {message}"
        self.logger.error(message)

    def log_debug(self, message: str, request_id: str = None):
        if request_id:
            message = f"[Request ID: {request_id}] {message}"
        self.logger.debug(message)