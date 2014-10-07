# -*- coding: utf-8 -*-

__author__ = 'Adrian Cruz'
__email__ = 'drincruz@gmail.com'
__version__ = '0.1.0'


class RomanNumConverter(object):

    def __init__(self, roman):
        self.__roman = roman
        self.__ROMANS_MAP = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def __add_chars(self, r0, r1):
        return self.__ROMANS_MAP[r0] + self.__ROMANS_MAP[r1]

    def to_integer(self):
        # Convert one-character Roman numeral
        if (len(self.__roman) == 1 and
            self.__roman in self.__ROMANS_MAP):
                return self.__ROMANS_MAP[self.__roman]
