import unittest
from FizzBuzz import FizzBuzzDetector


class TestStringMethods(unittest.TestCase):
    """Tests for FizzBuzz.py"""

    def test_FizzBuzzDetector_string(self):
        """Checking the "string" method"""
        a = FizzBuzzDetector('pythondeveloper')
        self.assertEqual(a.string, 'pythondeveloper')

    def test_FizzBuzzDetector_list(self):
        """Checking the "stolist" method"""
        a = FizzBuzzDetector('pythondeveloper')
        self.assertEqual(a.stolist, ['p', 'y', 't', 'h', 'o', 'n', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r'])

    def test_getOverlappings(self):
        """Checking the "getOverlappings" method"""
        a = FizzBuzzDetector('pythondeveloper')
        self.assertEqual(a.getOverlappings(), 1)

    def test_replaceFizzBuzz(self):
        """Checking the 'replaceFizzBuzz' method"""
        a = FizzBuzzDetector('python')
        self.assertEqual(a.replaceFizzBuzz(), 'pyFizzhBuzzFizz')


if __name__ == "__name__":
    unittest.main()
