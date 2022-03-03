"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
"""

import unittest
from human_readable_time import make_readable

class HumanReadableTimeTest(unittest.TestCase):
    def test_zero_seconds(self):
        self.assertEqual(make_readable(0), "00:00:00")

    def test_ten_seconds(self):
        self.assertEqual(make_readable(5), "00:00:05")

    def test_ten_minutes(self):
        self.assertEqual(make_readable(600), "00:10:00")
    
    def test_one_hour(self):
        self.assertEqual(make_readable(3600), "01:00:00")

    def test_complex_one(self):
        self.assertEqual(make_readable(1465), "00:24:25")

    def test_complex_two(self):
        self.assertEqual(make_readable(13913), "03:51:53")

    def test_complex_three(self):
        self.assertEqual(make_readable(87392), "24:16:32")

    def test_complex_four(self):
        self.assertEqual(make_readable(86399), "23:59:59")
    
    def test_complex_five(self):
        self.assertEqual(make_readable(359999), "99:59:59")
    