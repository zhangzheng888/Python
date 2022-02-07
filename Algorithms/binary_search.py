"""
Python Algorithm for Binary Search
"""

def binary_search(self, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    """
    Verifies whether the target was found in the target from linear search
    algorithm
    """
    if index is not None:
        return print("Target is in index ", index)
    else:
        return print("Target is not found in list")
