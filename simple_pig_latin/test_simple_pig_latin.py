"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples:

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import unittest
from simple_pig_latin import pig_it

class PigLatinTest(unittest.TestCase):

    def test_pig_latin_is_cool(self):
        self.assertEqual(pig_it("Pig latin is cool"), "igPay atinlay siay oolcay")

    def test_hello_world_with_punctuation(self):
        self.assertEqual(pig_it("Hello world !"), "elloHay orldway !")

    def test_this_is_my_string(self):
        self.assertEqual(pig_it("This is my string"), "hisTay siay ymay tringsay")

    def test_cancel_the_daily_scrum(self):
        self.assertEqual(pig_it("Cancel the Daily Scrum"), "ancelCay hetay ailyDay crumSay")

    def test_cancel_the_daily_scrum(self):
        self.assertEqual(pig_it("Today is a good day"), "odayTay siay aay oodgay ayday")