"""
Data Types: Numbers
We can use the type() function to know which class a variable or a value belongs
 to and isinstance() function to check if it belongs to a particular class.
"""

# Data Type Integer
number = 8

# Output: <class 'int'>
print(type(number))
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

# Data Type Float
number = -8.0

# Output: <class 'float'>
print(type(number))
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.

# Data Type Complex
complex_number = 5 + 3j

# Output: (8+3j)
print(complex_number + 3)

# Output: True
print(isinstance(complex_number, complex))
# Complex numbers are written with a "j" as the imaginary part.
