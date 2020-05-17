"""
Data Type: Tuples

Tuple Accessors

Indexing

The index operator [] to access an item in a tuple, where the index starts from 0.

A tuple having 6 elements will have indices from 0 to 5. Trying to access an index outside of the
tuple index range(6,7,... in this example) will raise an IndexError.

The index must be an integer, float or other types can't be used. This will result in TypeError.

Likewise, nested tuples are accessed using nested indexing.
"""

# Accessing tuple elements using indexing
simple_tuple = ('s', 'i', 'm', 'p', 'l', 'e')

print(simple_tuple[0])   # 's'
print(simple_tuple[5])   # 'e'

# IndexError: list index out of range
# print(simple_tuple[6])

# Index must be an integer
# TypeError: list indices must be integers, not float
# simple_tuple[2.0]

# nested tuple
nested_tuple = ("spice", [8, 4, 6], (1, 2, 3))

# nested index
print(nested_tuple[0][3])       # 'c'
print(nested_tuple[1][1])       # 4

"""
Negative Indexing

The index of -1 refers to the last item, -2 to the second last item and so on.
"""

# Negative indexing for accessing tuple elements
negative_tuple = ('h', 'o', 'r', 's', 'e', 's')

# Output: 't'
print(negative_tuple[-1])

# Output: 'p'
print(negative_tuple[-6])

"""
Slicing

A range of items in a tuple by using the slicing operator colon :.
"""

# Accessing tuple elements using slicing
slice_tuple = ('s', 'l', 'i', 'c', 'i', 'n', 'g', 's')

# elements 2nd to 4th
# Output: ('l', 'i', 'c')
print(slice_tuple[1:4])

# elements beginning to last
# Output: ('s', 's')
print(slice_tuple[:-7])

# elements 8th to end
# Output: ('g', 's')
print(slice_tuple[6:])

# elements beginning to end
# Output: ('s', 'l', 'i', 'c', 'i', 'n', 'g', 's')
print(slice_tuple[:])
