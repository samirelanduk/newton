from unittest import TestCase
from newton.functions import Function

class FunctionCreationTests(TestCase):

    def test_can_create_functions(self):
        f = Function()



class FunctionCallingTests(TestCase):

    def test_calling_bare_function_returns_input(self):
        f = Function()
        for n in range(10):
            self.assertEqual(n, f(n))
