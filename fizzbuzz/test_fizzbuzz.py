# Testing FizzBuzz

import unittest
from fizzbuzz import FizzBuzz

class FizzBuzzTests(unittest.TestCase):

    def test_if_value_is_a_multiple_of_three_use_fizz(self):
        self.assertEqual(FizzBuzz(3), [1, 2, "Fizz"])

    def test_if_value_is_a_multiple_of_five_use_buzz(self):
        self.assertEqual(FizzBuzz(5), [1, 2, "Fizz", 4, "Buzz"])

    def test_if_value_is_a_multiple_of_three_and_five_use_fizzbuzz(self):
        self.assertEqual(FizzBuzz(5), [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"])

if __name__ == '__main__':
    unittest.main()