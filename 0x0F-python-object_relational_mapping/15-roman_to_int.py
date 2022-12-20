#!/usr/bin/python3
"""
15-roman_to_int.py
Python program to convert Roman Numerals to Numbers
"""


def value(r):
    """ value() returns value of each Roman symbol
    Args:
        r: roman numeral to evaluate
    Returns:
        (int): Decimal value of a roman numeral or -1 if error
    """
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    """ roman_to_int() Calculates Decimal value of Roman Numbers
    Args:
        roman_string(str): roman number
    Returns:
        result (int): decimal number of entire roman number
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    result = 0
    i = 0
    while (i < len(roman_string)):
        # Get value of symbol at roman_string[i]
        s1 = value(roman_string[i])
        if (i + 1) < len(roman_string):
            # Get value of symbol roman_string[i + 1]
            s2 = value(roman_string[i + 1])
            # Compare both values
            if (s1 >= s2):
                # Value of current symbol >= next symbol
                result = result + s1
                i = i + 1
            else:
                # Value of current symbol is < next symbol
                result = result + s2 - s1
                i = i + 2
        else:
            result = result + s1
            i = i + 1
    return result
