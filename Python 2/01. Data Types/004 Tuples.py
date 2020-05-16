"""
Data Type: Tuples (Python 2.7)

A tuple in Python is similar to a list. The difference between the two is elements of a tuple can be
changed once it is assigned whereas the elements of a list can be changed.

A tuple is created by placing all the items (elements) inside parentheses (), separated by commas.
The parentheses are optional, but it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list,
string, etc.).
"""

# Empty tuple
empty_tuple = ()
print empty_tuple

# Tuple having integers
integer_tuple = (1, 2, 3)
print integer_tuple

# tuple with mixed datatypes
mixed_tuple = (1, "Hello", 3.4)
print mixed_tuple

# nested tuple
nested_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print nested_tuple

"""
A tuple can also be created without using parentheses. This is known as tuple packing.
"""

example_tuple = 3, 4.6, "dog"
print example_tuple

# tuple unpacking is also possible
a, b, c = example_tuple

print a      # 3
print b      # 4.6
print c      # dog

"""
Creating a tuple with one element is possible but it is a bit tricky.

Having one element within parentheses is not enough. A trailing comma to indicate that it is, in
fact, a tuple.
"""

not_tuple = ("hello")
print type(not_tuple)  # <class 'str'>

# Creating a tuple having one element
single_tuple = ("hello",)
print type(single_tuple)  # <class 'tuple'>

# Parentheses is optional
single_tuple = "hello",
print type(single_tuple)  # <class 'tuple'>
