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

    def to_integer(self):
        """
        Convert the Roman numeral to an integer

        :return:
        """
        # Convert one-character Roman numeral
        if (len(self.__roman) == 1 and
            self.__roman in self.__ROMANS_MAP):
                return self.__ROMANS_MAP[self.__roman]

        val = self.__ROMANS_MAP[self.__roman[0]]
        for ch in self.__roman[1:]:
            if val >= self.__ROMANS_MAP[ch]:
                val += self.__ROMANS_MAP[ch]
            if val < self.__ROMANS_MAP[ch]:
                val = -val + self.__ROMANS_MAP[ch]

        return val
