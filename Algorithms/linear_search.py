"""
Python Algorithm for Linear Search
"""

def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
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

"""
The time complexity of the linear search algorithm is O(n).

Linear search is rarely used practically because other search algorithms such
as the binary search algorithm and hash tables allow significantly
faster-searching comparison to Linear search.

Improve Linear Search Worst-Case Complexity

- if element found on the first try O(n) to O(1)
"""
