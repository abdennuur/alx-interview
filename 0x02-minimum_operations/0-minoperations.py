#!/usr/bin/python3
'''Minimum operations coding challenge.
'''


def minOperations(n):
    '''To compute the fewest nbr of operations needed to result
    in exactly nu H characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_cnt = 0
    clipbrd = 0
    dn = 1
    while dn < n:
        if clipbrd == 0:
            clipbrd = dn
            dn += clipbrd
            ops_cnt += 2
        elif n - dn > 0 and (n - dn) % dn == 0:
            clipbd = dn
            dn += clipbrd
            ops_cnt += 2
        elif clipbrd > 0:
            dn += clipbrd
            ops_cnt += 1
    return ops_cnt
