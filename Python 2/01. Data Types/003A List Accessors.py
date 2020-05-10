"""
Data Type: Lists (Python 2.7)

List Accessors

There are various ways to access the elements of a list.

List Index
The index operator [] to access an item in a list. Index starts from 0. A list having 5 elements
will have an index from 0 to 4.

Trying to access indexes other than these will raise an IndexError. The index must be an integer.
Float or other types of numbers as an index will result in TypeError.

Nested lists are accessed using nested indexing.
"""
# List indexing

example_list = ['t', 'o', 'y', 'o', 't', 'a']

# Output: p
print example_list[0]

# Output: o
print example_list[2]

# Output: e
print example_list[4]

# Nested List
nested_list = ["Supra", [2, 0, 2, 0]]

# Nested indexing
print nested_list[0][1]

print nested_list[1][3]

# Error! Only integer can be used for indexing
print nested_list[4.0]

"""
Negative indexing

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the
 second last item and so on.

 """

# Negative indexing in lists

example_list_2 = ['s', 'u', 'p', 'r', 'a']

print example_list_2[-1]

print example_list_2[-5]

"""
Slice Operator

The range of items in a list can be accessed by using the slicing operator :(colon).

"""

# List slicing in Python

my_list = ['c', 'r', 'e', 's', 's', 'i', 'd', 'a']

# elements 3rd to 5th
print my_list[2:5]

# elements beginning to 4th
print my_list[:-5]

# elements 6th to end
print my_list[5:]

# elements beginning to end
print my_list[:]
