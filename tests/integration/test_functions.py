from unittest import TestCase
import newton

class LinearFunctionTests(TestCase):

    def test(self):
        f = newton.Function()

        self.assertEqual(f(10), 10)
