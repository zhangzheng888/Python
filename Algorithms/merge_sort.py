def merge_sort(list):
    """
    Sorts the list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes overall O(n log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns 2 sublists: left and right

    Takes O(k log n) time
    """

    midpoint = len(list)//2
    left = list[:midpoint] # Python slice operation runs on O(k)
    right = list[midpoint:]
    return left, right

def split_iterative(list):
    """
    Divide the unsorted list at midpoint into sublists without using list slicing
    Returns 2 sublists: left and right

    Takes O(log n) time
    """

    midpoint = len(list)//2
    left = []
    right = []


    for index in range(len(list) - 1):
        if index < midpoint:
            left.append(list[index])
        elif index >= midpoint:
            right.append(list[index])
    return left, right


def merge(list_left, list_right):
    """
    Merges 2 lists (arrays), sorting them in the process
    Returns a new merged list

    Takes O(n) time
    """

    merged_list = []
    left_index = 0
    right_index = 0

    """
    The following condition assumes that both lists are of equal length
    When left or right list is shorter than the other, the while loop will exit
    when the shorter list ends
    """
    while left_index < len(list_left) and right_index < len(list_right):
        if list_left[left_index] < list_right[right_index]:
            merged_list.append(list_left[left_index])
            left_index += 1

        else:
            merged_list.append(list_right[right_index])
            right_index += 1

    """
    To account for uneven lists, a while loop will be constructed to account
    for shorter loop on either left or right_half
    """

    while left_index < len(list_left):
        merged_list.append(list_left[left_index])
        left_index += 1

    while right_index < len(list_right):
        merged_list.append(list_right[right_index])
        right_index += 1

    return merged_list


def verify_sorted(list):
    length = len(list)

    if length == 0 or length == 1:
        return True

    return list[0] < list [1] and verify_sorted(list[1:])
