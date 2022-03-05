"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements:

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

import unittest
from moving_zeros_to_the_end import move_zeros

class MovingZerosToTheEnd(unittest.TestCase):
    def test_move_zeros_simple_one(self):
        self.assertEqual(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])

    def test_move_zeros_simple_two(self):
        self.assertEqual(move_zeros([0, 0]), [0, 0])

    def test_move_zeros_simple_three(self):
        self.assertEqual(move_zeros([]), [])

    def test_move_zeros_complex_one(self):
        self.assertEqual(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]), [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_move_zeros_complex_two(self):
        self.assertEqual(move_zeros([10, 0, 3, 4, 0, 2, 0, 6, 0, 8, 0, 7, 7, 7, 0, 0, 1, 5, 8, 0, 3, 0, 0, 7, 2, 1]), [10, 3, 4, 2, 6, 8, 7, 7, 7, 1, 5, 8, 3, 7, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,])