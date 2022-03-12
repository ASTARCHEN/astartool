
class MethodNotFoundError(NotImplementedError):
    def __init__(self, *args):
        super().__init__(*args)


class ParameterError(ValueError):
    def __init__(self, *args):
        super().__init__(*args)
