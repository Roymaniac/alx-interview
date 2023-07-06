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

from collections import deque

def canUnlockAll(boxes):
    '''
    method that determines if all the boxes can be opened.
    '''
    # Set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # First box is already opened

    # Queue for BFS traversal
    queue = deque()
    queue.append(0)  # Add the first box to the queue

    # Perform BFS traversal
    while queue:
        current_box = queue.popleft()

        # Check all the keys in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
