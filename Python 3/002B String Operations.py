"""
Data Types: Strings

String Operations

Concatenation of Two or More Strings

Joining of two or more strings into a single one is called concatenation.

The + operator does this in Python.

The * operator can be used to repeat the string for a given number of times.
"""

string1 = 'First'
string2 = 'Second'

# using +
print('string1 + string2 = ',  string1 + string2)

# using *
print('string1 * 3 =',  string1 * 3)

"""
Writing two string literals together also concatenates them like + operator.

To concatenate strings in different lines, we can use parentheses.
"""

# two string literals together
# 'Separate ' 'Word!'
'Separate Word!'

# using parentheses
# 'Separate Words'
s = ('Separate '
     ...    'Words')
print(s)

"""
String Iteration

Using for loop it is possible to iterate through a string.
Here is an example to count the number of 'l' in a string.
"""

count = 0
for letter in 'Lollapalloza World':
    if(letter == 'l'):
        count += 1
print(count, 'letters found')

"""
String Membership

To check if a sub-string exists within a string or not, using the keyword in.
"""

'a' in 'anagram'
# True

'at' not in 'cattle'
# False

"""
Built-in String Functions

Some of the commonly used ones are enumerate() and len().
The enumerate() function returns an enumerate object. It contains the index and value of all the
 items in the string as pairs. This can be useful for iteration.

"""

sample_string = 'bladder'

# enumerate()
list_enumerated = list(enumerate(sample_string))
print('list(enumerate(sample_string) = ', list_enumerated)

# character count
print('len(sample_string) = ', len(sample_string))
