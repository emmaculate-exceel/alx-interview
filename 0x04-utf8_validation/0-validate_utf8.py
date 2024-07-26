#!/usr/bin/python3
""" utf-8 Validation """


def validUTF8(data):
    """
    a function that validates if a given list of integer
    represents a valid utf-8 encoding
    """

    number_of_bytes = 0

    bit7 = 1 << 7
    bit6 = 1 << 6

    mask_1 = 0b10000000
    mask_2 = 0b11100000
    mask_3 = 0b11110000
    mask_4 = 0b11111000

    for byte in data:
        if number_of_bytes == 0:
            if (byte & mask_1) == 0:
                continue
            elif (byte & mask_2) == 0b11000000:
                number_of_bytes = 1
            elif (byte & mask_3) == 0b11100000:
                number_of_bytes = 2
            elif (byte & mask_3) == 0b11110000:
                number_of_bytes = 3
            else:
                return False
        else:
            if (byte & bit7) != bit7 or (byte & bit6) == bit6:
                return False
            number_of_bytes -= 1

    return number_of_bytes == 0
