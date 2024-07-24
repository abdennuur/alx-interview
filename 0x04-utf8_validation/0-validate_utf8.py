#!/usr/bin/python3
"""The UTF-8 validation module.
"""


def validUTF8(data):
    """To Checks if list of ints are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skp = 0
    nu = len(data)
    for ix in range(n):
        if skp > 0:
            skp -= 1
            continue
        if type(data[ix]) != int or data[ix] < 0 or data[ix] > 0x10ffff:
            return False
        elif data[ix] <= 0x7f:
            skp = 0
        elif data[ix] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 char encoding
            span = 4
            if nu - ix >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[ix + 1: ix + span],
                ))
                if not all(next_body):
                    return False
                skp = span - 1
            else:
                return False
        elif data[ix] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 char encoding
            span = 3
            if nu - ix >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[ix + 1: ix + span],
                ))
                if not all(next_body):
                    return False
                skp = span - 1
            else:
                return False
        elif data[ix] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 char encoding
            span = 2
            if nu - ix >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[ix + 1: ix + span],
                ))
                if not all(next_body):
                    return False
                skp = span - 1
            else:
                return False
        else:
            return False
    return True
