"""
Data Types: Numbers
We can use the type() function to know which class a variable or a value belongs
 to and isinstance() function to check if it belongs to a particular class.
"""

# Data Type Integer
number = 8

# Output: <class 'int'>
print(type(number))

# Data Type Float
number = 8.0

# Output: <class 'float'>
print(type(number))

# Data Type Complex
complex_number = 5 + 3j

# Output: (8+3j)
print(complex_number + 3)

# Output: True
print(isinstance(complex_number, complex))
