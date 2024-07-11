#!/usr/bin/python3
'''The Min operations coding challenge.
'''


def minOperations(n):
    '''To compute the fewest nbr of operations needed to result
    in exactly n 'H' characters.
    '''
    if not isinstance(n, int):
        return 0
    ops_cnt = 0
    clipbrd = 0
    dn = 1
    # to print('H', end='')
    while dn < n:
        if clipbrd == 0:
            # to init (the first copy all and paste)
            clipbrd = dn
            dn += clipbrd
            ops_cnt += 2
            # to print('-(11)->{}'.format('H' * done), end='')
        elif n - dn > 0 and (n - dn) % dn == 0:
            # to copy all and paste
            clipbrd = dn
            dn += clipbrd
            ops_cnt += 2
            # to print('-(11)->{}'.format('H' * done), end='')
        elif clipbrd > 0:
            # to paste
            dn += clipbrd
            ops_cnt += 1
            # to print('-(01)->{}'.format('H' * done), end='')
    # to print('')
    return ops_cnt
