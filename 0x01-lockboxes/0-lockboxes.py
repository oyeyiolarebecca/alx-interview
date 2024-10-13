#!/usr/bin/env python3
def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set([0])  # Start with the first box unlocked
    keys = set(boxes[0])  # Initially, we have keys from the first box
    
    while keys:
        new_key = keys.pop()  # Take a key from the set
        if new_key < n and new_key not in unlocked:
            unlocked.add(new_key)  # Unlock the corresponding box
            keys.update(boxes[new_key])  # Add keys from the newly unlocked box
    
    # If the number of unlocked boxes equals the total number of boxes, return True
    return len(unlocked) == n
