"""
You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. 
After ordering these strings in dictionary order, return the middle term. (If the sequence has a even 
length n, define its middle term to be the (n/2)th term.)
"""

import unittest
from middle_permutation import middle_permutation

class HumanReadableTimeTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(middle_permutation("abc"),"bac")

    def test_two(self):
        self.assertEqual(middle_permutation("abcd"),"bdca")

    def test_three(self):
        self.assertEqual(middle_permutation("abcdx"),"cbxda")
    
    def test_four(self):
        self.assertEqual(middle_permutation("abcdxg"),"cxgdba")

    def test_five(self):
        self.assertEqual(middle_permutation("abcdxgz"),"dczxgba")
    
    def test_six(self):
        self.assertEqual(middle_permutation("biqyuhjvzcfkrxgodltmpsena"),"mlzyxvutsrqponkjihgfedcba")
    
    def test_seven(self):
        self.assertEqual(middle_permutation("yrwvbtezsilcqakmhjndgxp"),"mlzyxwvtsrqpnkjihgedcba")
    
    def test_eight(self):
        self.assertEqual(middle_permutation("laiyxtbpohc"),"liyxtpohcba")
    
    def test_nine(self):
        self.assertEqual(middle_permutation("ijtqalxprdmgwfkvuyhbszcnoe"),"mzyxwvutsrqponlkjihgfedcba")