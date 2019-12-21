import unittest

from Compare import Compare

class CompareTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(CompareTests, self).__init__(*args, **kwargs)
        self.compare = Compare()


    def test_return_hundred_exact_same(self):

        value1 = "Danilo"
        value2 = "Danilo"

        self.compare.compare(value1, value2)
        value_to_test = self.compare.get_strength()
        
        self.assertEquals(100, value_to_test)


    def test_return_hundred_exact_same_multiple_strings(self):

        value1 = "Danilo Silva"
        value2 = "Danilo Silva"

        self.compare.compare(value1, value2)
        value_to_test = self.compare.get_strength()

        self.assertEquals(100, value_to_test)


    def test_return_hundred_exact_same_very_long_string(self):

        value1 = "This is a very long string to compare"
        value2 = "This is a very long string to compare"

        self.compare.compare(value1, value2)
        value_to_test = self.compare.get_strength()

        self.assertEquals(100, value_to_test)

    
    def test_return_zero_different_single_strings(self):

        value1 = "Alfa"
        value2 = "Beta"

        self.compare.compare(value1, value2)
        value_to_test = self.compare.get_strength()

        self.assertEquals(0, value_to_test)


    def test_return_over_90_strength_similar_strings_and_below_100(self):

        value1 = "This is a string that is very"
        value2 = "This is a string that is very similar"


if __name__ == '__main__':
    unittest.main()