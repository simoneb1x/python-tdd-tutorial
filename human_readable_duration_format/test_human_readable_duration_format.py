"""
Your task in order to complete this Kata is to write a function which formats a duration, 
given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
"""

import unittest
from human_readable_duration_format import format_duration

class HumanReadableDurationFormat(unittest.TestCase):
    def test_one_second(self):
        self.assertEqual(format_duration(1), "1 second")

    def test_sixtytwo_seconds(self):
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")
    
    def test_twominutes(self):
        self.assertEqual(format_duration(120), "2 minutes")
    
    def test_onehour(self):
        self.assertEqual(format_duration(3600), "1 hour")
    
    def complex(self):
        self.assertEqual(format_duration(3662), "1 hour, 1 minute and 2 seconds")