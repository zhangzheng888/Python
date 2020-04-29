"""
Data Types: Strings

String Access/Slicing

Individual characters in a string using indexing and a range of characters using slicing.
Index starts from 0.

Python allows negative indexing for its sequences.
The range can be used to access items in a string by using the slicing operator (colon).
The index of -1 refers to the last item, -2 to the second last item etc.
"""

sample_string = 'teslarati'
print('string =  ', sample_string)

# first character
print('string[0] = ', sample_string[0])

# last character
print('string[-1] = ', sample_string[-1])

# slicing 2nd to 5th character
print('string[1:5] = ', sample_string[1:5])

# slicing 6th to 2nd last character
print('string[5:-2] = ', sample_string[5:-2])

"""
Accessing a character out of index range will raise an IndexError.
The index must be an integer. We can't use float or other types, this will result in a TypeError.
"""

# index must be in range
sample_string[15]
# IndexError: string index out of range

# index must be an integer
sample_string[1.5]
# TypeError: string indices must be integers

"""
Slicing can be best visualized by considering the index to be between the elements(characters) in a
string.

By defining a range, this will dictate the index that will slice the portion from the string.

String Deletion

Strings are immutable. This means that elements of a string cannot be changed once it has been
assigned.

We cannot delete or remove characters from a string. But deleting the string entirely is possible
using the keyword del.
"""

del sample_string[1]
# TypeError: 'str' object doesn't support item deletion

del sample_string
