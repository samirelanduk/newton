from unittest import TestCase
import newton

class LinearFunctionTests(TestCase):

    def test(self):
        f = newton.Function()
        self.assertEqual(f(10), 10) # f(x) = x

        f = newton.Function(newton.Multiplier(5))
        self.assertEqual(f(10), 50) # f(x) = 5x
