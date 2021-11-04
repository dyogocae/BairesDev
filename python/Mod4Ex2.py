# -*- coding: utf-8 -*-
"""
Module 4
Ex 2) Create a unit testing to extensively test all possibilities of the 
function created in the regex exercise above.

@author: dyogo
"""

import re       #Regex library
import unittest #unit tests

class TestRegexMethod(unittest.TestCase):

    def test_regex(self):
        self.assertRegex('abc_xyz', r'^[a-z]+_[a-z]+$')

    def test_regex_incomplete(self):
        self.assertRegex('abc', r'^[a-z]+_[a-z]+$')
    
    def test_regex_upper(self):
        self.assertRegex('aBC_pod', r'^[a-z]+_[a-z]+$')

if __name__ == '__main__':
    unittest.main()
