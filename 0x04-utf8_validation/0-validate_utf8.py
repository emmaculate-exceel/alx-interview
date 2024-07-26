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

    for byte in data:
        byte = byte & 0xFF

        if number_of_bytes == 0:

            if (byte & bit7) == 0:
                continue
            elif (byte & (bit7 | bit6)) == bit7:
                # != 0 and (byte & bit6) == 0:
                return False
            elif (byte & bit7) != 0 and (byte & bit6) == 0:
                if (byte & (bit7 >> 1)) == 0:
                    number_of_bytes = 1
                elif (byte & (bit7 >> 2)) == 0:
                    number_of_bytes = 2
                elif (byte & (bit7 >> 3)) == 0:
                    number_of_bytes = 3
                else:
                    return False
            else:
                if (byte & (bit7 | bit6)) != bit6:  # 0 and (byte & bit6) == 0:
                    number_of_bytes -= 1
                else:
                    return False
    return number_of_bytes == 0
