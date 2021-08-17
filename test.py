import unittest
from FizzBuzz import FizzBuzzDetector


class TestStringMethods(unittest.TestCase):
    """Tests for FizzBuzz.py"""

    def test_FizzBuzzDetector_string(self):
        """Checking the "string" method"""
        test_string = FizzBuzzDetector("pythondeveloper")
        self.assertEqual(test_string.string, "pythondeveloper")

    def test_getOverlappings(self):
        """Checking the "getOverlappings" method"""
        test_string = FizzBuzzDetector("pythondeveloper")
        self.assertEqual(test_string.getOverlappings(), 1)

    def test_replaceFizzBuzz(self):
        """Checking the 'replaceFizzBuzz' method"""
        test_string = FizzBuzzDetector("pythonic")
        self.assertEqual(test_string.replaceFizzBuzz(), "pyFizzhBuzzFizzic")

    def test_check_isalpha(self):
        """Checking for occurrence of mismatched symbols in a string"""
        with self.assertRaises(SyntaxError) as context:
            test_string = FizzBuzzDetector("pytho5nic")
            test_string.replaceFizzBuzz()

        self.assertTrue(
            "String should contain only letters of the english alphabet"
            in str(context.exception)
        )

    def test_check_islower(self):
        """Checking the case of a string"""
        with self.assertRaises(SyntaxError) as context:
            test_string = FizzBuzzDetector("Pythonic")
            test_string.replaceFizzBuzz()

        self.assertTrue(
            "String should contain only lowercase letters" in str(context.exception)
        )

    def test_check_length(self):
        """Checking the length of a string"""
        with self.assertRaises(SyntaxError) as context:
            test_string = FizzBuzzDetector("P")
            test_string.replaceFizzBuzz()

        self.assertTrue(
            "The string length must be between 7 and 100 characters inclusive"
            in str(context.exception)
        )


if __name__ == "__name__":
    unittest.main()
