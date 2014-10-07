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

        val = 0
        chars = list(self.__roman)
        i = 0
        while i < len(chars)-1:
            if self.__ROMANS_MAP[chars[i]] >= self.__ROMANS_MAP[chars[i+1]]:
                val += self.__ROMANS_MAP[chars[i]]
                i += 1
            #else self.__ROMANS_MAP[chars[i]] < self.__ROMANS_MAP[chars[i+1]]:
            else:
                val += (self.__ROMANS_MAP[chars[i+1]] - self.__ROMANS_MAP[chars[i]])
                i += 2

        if i != len(chars):
            val += self.__ROMANS_MAP[chars[i]]

        return val

