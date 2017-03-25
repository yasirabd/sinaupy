from unittest import TestCase
from bagi_lima import bagi_lima

class Test_PlusFive(TestCase):
    def setUp(self):
        self.test_in = [10, 11, 12, 15]
        self.expected_output = [2, 2.2, 2.4, 3]

    def test_plus_five(self):
        test_output = []

        for number in self.test_in:
            test_output.append(bagi_lima(number))

        self.assertEqual(self.expected_output, test_output)
