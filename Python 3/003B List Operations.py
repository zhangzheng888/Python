"""
Data Type: Lists

Change or Add elements to a List

Lists are mutable, meaning their elements can be changed unlike string or tuple.

We can use assignment operator (=) to change an item or a range of items.
"""

# Correcting mistake values in a list
odd = [2, 0, 9, 9]

# change the 1st item
odd[0] = 1

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)

"""
append() method can be used to add single item to list or add several items using extend() method.
"""

# Appending and Extending lists in Python
pi_numerals = [3, 1, 4]

pi_numerals.append(7)

print(pi_numerals)

pi_numerals.extend([9, 11, 13])

print(pi_numerals)

"""
List concatenation

Use + operator to combine two lists.

The * operator repeats a list for the given number of times.

"""

# Concatenating and repeating lists

odd_numbers = [1, 3, 5]

print(odd_numbers + [9, 7, 5])

print(["corolla"] * 3)

"""
List Insertion

An item can be inserted at a desired location by using the method insert() or insert multiple items
by squeezing it into an empty slice of a list.

"""
# Demonstration of list insert() method

prime_numbers = [2, 7]

prime_numbers.insert(3, 5)

print(prime_numbers)

prime_numbers[2:2] = [5, 7]

print(prime_numbers)
