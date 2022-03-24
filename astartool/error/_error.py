
class MethodNotFoundError(NotImplementedError):
    def __init__(self, *args):
        super().__init__(*args)


class ParameterTypeError(TypeError):
    def __init__(self, *args):
        super().__init__(*args)


class ParameterValueError(ValueError):
    def __init__(self, *args):
        super().__init__(*args)


class ParameterError(ParameterTypeError, ParameterValueError):
    def __init__(self, *args):
        super().__init__(*args)
