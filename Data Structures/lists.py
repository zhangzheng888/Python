"""
Arrays - Python Lists
"""

"""
Python Lists are heterogenous structures that can store any kind of value.

Typically, Arrays is stored as a contiguous data structure.

Python Lists stores contiguous blocks but instead of storing the data
themselves, the list stores pointers to the memory address which
actually holds the data.

Elements inside the Array are identified using a value known as the index.

The index are used to access and read the value.
"""

new_list = [1, 2, 3]

"""
The data in the list can be accessed by using the index
"""
result = new_list[0]

"""
The following will create an out of bounds exception because
the memory address returned is not part of the array data structure,
therefore can't be accessed by the array.

In Python, this will be an IndexError: list index out of range
"""
out_of_bounds = new_list[5]


"""
Search in Lists or Arrays can be performed 1 of 2 ways
"""

"""
1. Using linear search in if ...
"""
if 1 in new_list: print(True)

"""
2. Using linear search in for ...
"""
for n in new_list:
    if n == 1:
        print(True)

        break

"""
Items can be added to lists by using the append function
"""

new_list.append(4)

"""
Python List allocates a set amount of contiguous memory.
The growth pattern is as follows:
0, 4, 8, 16, 25, 35, 46 ...

This means as the list size approaches the listed above,
an internal resize is called to expand the list size to the
next allotted size
"""

"""
Python List has another function extend, which takes each element
from the added list and makes a series of append calls to add the
elements to the new list
"""

new_list.extend([4, 5, 6])
