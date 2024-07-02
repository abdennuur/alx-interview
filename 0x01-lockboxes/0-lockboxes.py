#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''To check if all boxes in list of boxes containing the keys
    (indices) to the other boxes can be unlocked given that first
    unlocked box.
    '''
    nBoxes = len(boxes)
    seenBoxes = set([0])
    unseenBoxes = set(boxes[0]).difference(set([0]))
    while len(unseenBoxes) > 0:
        boxIdx = unseenBoxes.pop()
        if not boxIdx or boxIdx >= nBoxes or boxIdx < 0:
            continue
        if boxIdx not in seenBoxes:
            unseenBoxes = unseenBoxes.union(boxes[boxIdx])
            seenBoxes.add(boxIdx)
    return nBoxes == len(seenBoxes)
