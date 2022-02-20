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
Python List has an insert function as well, working similarly
to append, but can be anywhere within the index as opposed to
the front.
"""

"""
Python List has another function extend, which takes each element
from the added list and makes a series of append calls to add the
elements to the new list
"""

new_list.extend([4, 5, 6])

"""
Extend has a runtime complexity of O(k) where k is the number
of elements in the list that is being added
"""

"""
Python List also contains a delete operation.
"""


"""
Python List Comprehension

basic format: new_list = [transform sequence[filter]]

Example 1:
Get values within a range

under_10 = [x for x in range(10)]


Example 2:
Get squared values

squares = [x**2 for x in range(10)]


Example 3:
Get odd numbers using modulus

odds = [x for x in range(10) if x%2 == 1]

Example 4:
Get multiples of 10

ten_x = [x * 10 for x in range(10)]

Example 5:
Get all numbers from a string

string = "1 is 2 is 3 to 4"

nums = [x for x in string if x.isnumeric()]

Example 6:
Get index of item in list

list = ['Manny', 'Luis', 'Eddy']

index = [k for k, v in enumerate(list) if k == 'Luis']

Example 7:
Delete an item from a list

old_list = [x for x in 'ABCDEF']

new_list = [x for x in old_list if x != 'F']


If-else condition in Comprehension
must come before iteration
Example:

nums = [5, 8, 7, 3, 4, 1]

new_list = [x if x%2 != 1 else x*10 for x in nums]

Nested loop iteration for 2D list

Example:

a = [[1, 2][3, 4]]

b is the subset, x is the values
new_list = [x for b in a for x in b]
"""
