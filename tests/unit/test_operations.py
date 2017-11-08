from unittest import TestCase
from newton.operations import Multiplier

class MultiplierCreationTests(TestCase):

    def test_can_create_multiplier(self):
        mul = Multiplier(9)
        self.assertEqual(mul._value, 9)



class MultiplierReprTests(TestCase):

    def test_multiplier_repr(self):
        mul = Multiplier(9)
        self.assertEqual(str(mul), "<Multiplier (×9)>")



class MultiplierActionTests(TestCase):

    def test_can_use_multiplier(self):
        mul = Multiplier(9)
        self.assertEqual(mul(4), 36)
