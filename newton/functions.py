"""Contains the Function class."""

class Function:
    """A mathematical function. By default it is the identity function."""

    def __init__(self, *operations):
        self._operations = list(operations)


    def __call__(self, arg):
        output = arg
        for operation in self._operations:
            output = operation(output)
        return output
