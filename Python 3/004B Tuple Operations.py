"""
Data Type: Tuples

Tuple Operations

Indexing

Changing a Tuple

Unlike lists, tuples are immutable.

This means that elements of a tuple cannot be changed once they have been assigned. But, if the
 element is itself a mutable data type like list, its nested items can be changed.

A tuple can also be assigned to different values (reassignment).
"""

# Changing tuple values
example_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# example_tuple[1] = 9

# However, item of mutable element can be changed
example_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5])
print(example_tuple)

# Tuples can be reassigned
example_tuple = ('r', 'e', 'a', 's', 's', 'i', 'g', 'n')

# Output: ('r', 'e', 'a', 's', 's', 'i', 'g', 'n')
print(example_tuple)

"""
Concatenation
The + operator can be used to combine two tuples.

Repeat
To repeat the elements in a tuple for a given number of times, the * operator is used.

Both + and * operations result in a new tuple.
"""

# Concatenation
# Output: (2, 3, 4, 5)
print((2, 3) + (4, 5))

# Repeat
# Output: ('Threepeat', 'Threepeat', 'Threepeat')
print(("Threepeat",) * 3)

"""
Deletion

Because tuples are immutable, it means that items cannot be deleted or removed FROM a tuple.

Deleting a tuple ENTIRELY, however, is possible using the keyword del.

"""

# Deleting tuples
deleting_tuple = ('d', 'e', 'l', 'e', 't', 'i', 'o', 'n')

# can't delete items
# TypeError: 'tuple' object doesn't support item deletion
# del deleting_tuple[3]

# Can delete an entire tuple
del deleting_tuple

# NameError: name 'my_tuple' is not defined
print(deleting_tuple)
