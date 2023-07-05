class DuplicationException(Exception):
    def __init__(self, message):
        self.message = message


class ForeignKeyException(Exception):
    def __init__(self, message):
        self.message = message


class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
