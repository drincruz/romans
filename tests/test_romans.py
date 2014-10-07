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

    def test_four_combined(self):
        roman = RomanNumConverter('IIII')
        self.assertEqual(4, roman.to_integer())

    def test_four_combined_2(self):
        roman = RomanNumConverter('XXXX')
        self.assertEqual(40, roman.to_integer())

    def test_13(self):
        roman = RomanNumConverter('XIII')
        self.assertEqual(13, roman.to_integer())

    def test_207(self):
        roman = RomanNumConverter('CCVII')
        self.assertEqual(207, roman.to_integer())

    def test_1066(self):
        roman = RomanNumConverter('MLXVI')
        self.assertEqual(1066, roman.to_integer())

    def test_4(self):
        roman = RomanNumConverter('IV')
        self.assertEqual(4, roman.to_integer())

    def test_9(self):
        roman = RomanNumConverter('IX')
        self.assertEqual(9, roman.to_integer())

    def test_40(self):
        roman = RomanNumConverter('XL')
        self.assertEqual(40, roman.to_integer())

    def test_90(self):
        roman = RomanNumConverter('XC')
        self.assertEqual(90, roman.to_integer())

    def test_400(self):
        roman = RomanNumConverter('CD')
        self.assertEqual(400, roman.to_integer())

    def test_900(self):
        roman = RomanNumConverter('CM')
        self.assertEqual(900, roman.to_integer())

    def test_1904(self):
        roman = RomanNumConverter('MCMIV')
        self.assertEqual(1904, roman.to_integer())

    def test_1954(self):
        roman = RomanNumConverter('MCMLIV')
        self.assertEqual(1954, roman.to_integer())

    def test_1990(self):
        roman = RomanNumConverter('MCMXC')
        self.assertEqual(1990, roman.to_integer())

    def test_2014(self):
        roman = RomanNumConverter('MMXIV')
        self.assertEqual(2014, roman.to_integer())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()