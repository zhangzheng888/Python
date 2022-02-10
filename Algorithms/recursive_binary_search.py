"""
Python Algorithm for Recursive Binary Search
"""

def recursive_binary_search(list, target):
    """
    Base case
    """
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                start = midpoint + 1
                new_list = list[start:]
                return recursive_binary_search(self, new_list, target)
            elif list[midpoint] > target:
                end = midpoint
                new_list = list[:end]
                return recursive_binary_search(self, new_list, target)

def verify(result):
    """
    Verifies whether the target was found in the target from linear search
    algorithm
    """
    print("Target found: ", result)
