#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_romans
----------------------------------

Tests for `romans` module.
"""

import unittest

from romans import RomanNumConverter


class TestRomans(unittest.TestCase):

    def setUp(self):
        pass

    def test_single_char_romans(self):
        roman = RomanNumConverter('I')
        self.assertEqual(1, roman.to_integer())

    def test_single_char_roman_x(self):
        roman = RomanNumConverter('X')
        self.assertEqual(10, roman.to_integer())

    def test_add_combined_romans(self):
        roman = RomanNumConverter('II')
        self.assertEqual(2, roman.to_integer())

    def test_add_combined_romans_3(self):
        roman = RomanNumConverter('III')
        self.assertEqual(3, roman.to_integer())

    def test_subtract_combined_romans(self):
        roman = RomanNumConverter('IV')
        self.assertEqual(4, roman.to_integer())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()