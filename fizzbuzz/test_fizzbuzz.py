"""
Return an array containing the numbers from 1 to N, where N is the parametered value.

Replace certain values however if any of the following conditions are met:

If the value is a multiple of 3: use the value "Fizz" instead
If the value is a multiple of 5: use the value "Buzz" instead
If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
"""

import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTests(unittest.TestCase):

    def test_if_value_is_a_multiple_of_three_use_fizz(self):
        self.assertEqual(FizzBuzz(3), [1, 2, "Fizz"])

    def test_if_value_is_a_multiple_of_five_use_buzz(self):
        self.assertEqual(FizzBuzz(5), [1, 2, "Fizz", 4, "Buzz"])

    def test_if_value_is_a_multiple_of_three_and_five_use_fizzbuzz(self):
        self.assertEqual(FizzBuzz(15), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"])

if __name__ == '__main__':
    unittest.main()