#!/usr/bin/python3
'''
Write a method that determines if all the boxes can be opened.
Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
'''

def canUnlockAll(boxes):
    """ method that verifies unlocking """
    if type(boxes) is not list or not all(type(box) is list for box in boxes):
        return False
    # check if list is empty
    if len(boxes) == 0:
        return False
    # check if only exist one box
    if len(boxes) == 1:
        return True
    # check if first box is empty
    if not boxes[0] and len(boxes) > 1:
        return False
    # dictionary of all boxes, all boxes are lock here
    unlock = {k: False for k in range(len(boxes))}
    # unlock first box
    unlock[0] = True
    # List of all key's first box
    keys = [key for key in boxes[0]]
    # Process of unlock boxes
    while keys:
        new_key = []
        for key in keys:
            if key in unlock.keys() and unlock[key] is False:
                new_key += boxes[key]
                unlock[key] = True
        # If all boxes unlock return True
        if all(unlock.values()) and len(unlock) == len(boxes):
            return True
        # Change keys for the new keys to check
        keys = new_key
    return False

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
