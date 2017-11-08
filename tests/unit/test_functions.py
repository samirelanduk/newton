from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from newton.functions import Function

class FunctionCreationTests(TestCase):

    def test_can_create_functions(self):
        f = Function()
        self.assertEqual(f._operations, [])


    def test_can_create_function_with_operations(self):
        operation1, operation2 = Mock(), Mock()
        f = Function(operation1, operation2)
        self.assertEqual(f._operations, [operation1, operation2])



class FunctionCallingTests(TestCase):

    def test_calling_bare_function_returns_input(self):
        f = Function()
        for n in range(10):
            self.assertEqual(n, f(n))


    def test_function_applies_operators(self):
        op1, op2 = MagicMock(), MagicMock()
        op1.return_value = 20
        op2.return_value = 40
        f = Function(op1, op2)
        val = f(10)
        op1.assert_called_with(10)
        op2.assert_called_with(20)
        self.assertEqual(val, 40)
