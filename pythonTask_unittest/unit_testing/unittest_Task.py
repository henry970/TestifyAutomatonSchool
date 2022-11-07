import unittest
import unittest

class TestAssertIs(unittest.TestCase):
    def testString(self):
        a = 'JavaScript'
        b = 'JavaScript'
        self.assertIs(a, b)


class TestAssertNotEqual(unittest.TestCase):
    def test_number(self):
        a = 38
        b = 60
        self.assertIsNot(a, b)
