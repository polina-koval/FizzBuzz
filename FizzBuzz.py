class FizzBuzzDetector:
    """The class implements the logic of replacing every 3rd letter with Fizz, and every fifth with Buzz"""

    def __init__(self, string):
        """Constructor"""
        self.string = string
        self.stolist = list(string)

    def getOverlappings(self):
        """returns the number of hits for the incoming string for 'FizzBuzz' only"""
        return len(self.string) // 15

    def replaceFizzBuzz(self):
        """replaces every third word in the letter to Fizz, and every fifth letter in the word to Buzz"""
        res = []
        for i in range(len(self.stolist)):
            # Number divisible by 15,(divisible
            # by both 3 & 5), add 'FizzBuzz'
            # in place of symbol
            if (i + 1) % 15 == 0:
                res.append("FizzBuzz")
            # Number divisible by 3, add 'Fizz'
            # in place of the symbol
            elif (i + 1) % 3 == 0:
                res.append("Fizz")
            # Number divisible by 5,
            # add 'Buzz' in
            # place of the symbol
            elif (i + 1) % 5 == 0:
                res.append("Buzz")
            # add symbol from
            # input string
            else:
                res.append(self.stolist[i])
        return "".join(res)
