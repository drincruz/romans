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

        # Initialize index, i and value, val
        i, val = 0, 0

        # Iterate through Roman numeral
        while i < len(self.__roman)-1:
            # If the value of the first character is greater than
            # the value of the next one, just add the value
            if self.__ROMANS_MAP[self.__roman[i]] >= self.__ROMANS_MAP[self.__roman[i+1]]:
                val += self.__ROMANS_MAP[self.__roman[i]]
                i += 1
            # Else, add the difference between the two
            else:
                val += (self.__ROMANS_MAP[self.__roman[i+1]] - self.__ROMANS_MAP[self.__roman[i]])
                i += 2

        # If we have left over characters to parse,
        # just add that to the val
        if i != len(self.__roman):
            val += self.__ROMANS_MAP[self.__roman[i]]

        return val
