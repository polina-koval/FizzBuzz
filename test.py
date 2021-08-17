import unittest
from FizzBuzz import FizzBuzzDetector


class TestStringMethods(unittest.TestCase):
    """Tests for FizzBuzz.py"""

    def test_FizzBuzzDetector_string(self):
        """Checking the "string" method"""
        test_string = FizzBuzzDetector("pythondeveloper")
        self.assertEqual(test_string.string, "pythondeveloper")

    def test_FizzBuzzDetector_list(self):
        """Checking the "stolist" method"""
        test_string = FizzBuzzDetector("pythondeveloper")
        self.assertEqual(
            test_string.stolist,
            ["p", "y", "t", "h", "o", "n", "d", "e", "v", "e", "l", "o", "p", "e", "r"],
        )

    def test_getOverlappings(self):
        """Checking the "getOverlappings" method"""
        test_string = FizzBuzzDetector("pythondeveloper")
        self.assertEqual(test_string.getOverlappings(), 1)

    def test_replaceFizzBuzz(self):
        """Checking the 'replaceFizzBuzz' method"""
        test_string = FizzBuzzDetector("python")
        self.assertEqual(test_string.replaceFizzBuzz(), "pyFizzhBuzzFizz")


if __name__ == "__name__":
    unittest.main()
