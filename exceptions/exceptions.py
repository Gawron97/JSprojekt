

class WrongPriceException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCategoryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectTypeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class WrongDateError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class WrongLimitException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
