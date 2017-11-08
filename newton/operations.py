
class Multiplier:

    def __init__(self, value):
        self._value = value


    def __repr__(self):
        return "<Multiplier (×{})>".format(self._value)


    def __call__(self, other):
        return self._value * other
