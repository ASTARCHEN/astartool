
class MethodNotFoundError(NotImplementedError):
    def __init__(self, *args):
        super().__init__(*args)
