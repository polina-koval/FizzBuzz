class FizzBuzzDetector:
    """The class implements the logic of replacing every 3rd letter with Fizz, and every fifth with Buzz"""

    def __new__(cls, string: str, *args, **kwargs):
        if len(string) < 7 or len(string) > 30:
            raise SyntaxError(
                "The string length must be between 7 and 100 characters inclusive"
            )
        elif not string.islower():
            raise SyntaxError("String should contain only lowercase letters")
        elif not string.isalpha():
            raise SyntaxError(
                "String should contain only letters of the english alphabet"
            )
        return object.__new__(cls)

    def __init__(self, string: str):
        """Constructor"""
        self.string = string

    def getOverlappings(self):
        """returns the number of hits for the incoming string for 'FizzBuzz' only"""
        return len(self.string) // 15

    def replaceFizzBuzz(self):
        """replaces every third word in the letter to Fizz, and every fifth letter in the word to Buzz"""
        res = []
        for i in range(len(self.string)):
            # Number divisible by 15,(divisible by both 3 & 5), add 'FizzBuzz' in place of symbol
            if (i + 1) % 15 == 0:
                res.append("FizzBuzz")
            # Number divisible by 3, add 'Fizz' in place of the symbol
            elif (i + 1) % 3 == 0:
                res.append("Fizz")
            # Number divisible by 5, add 'Buzz' in place of the symbol
            elif (i + 1) % 5 == 0:
                res.append("Buzz")
            # add symbol from input string
            else:
                res.append(self.string[i])
        return "".join(res)
