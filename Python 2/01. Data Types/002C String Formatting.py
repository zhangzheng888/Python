"""
Data Types: Strings (Python 2.7)

String Formatting

Escape Sequence

Escape sequence starts with a backslash and is interpreted differently. If a single quote is used to
represent a string, all the single quotes inside the string must be escaped. Similar is the case with
double quotes.
"""

# using triple quotes
print '''He said, "What's that?"'''

# escaping single quotes
print 'He said, "What\'s that?"'

# escaping double quotes
print "He said, \"What's that?\""

print "C:\\Python32\\Lib"
# Output
# C:\Python32\Lib

print "This is printed\nin two lines"
# Output
# This is printed
# in two lines

print "This is \x48\x45\x58 representation"
# Output
# This is HEX representation

"""
Raw String

To ignore the escape sequences inside a string, place r or R in front of the string. This will imply
that it is a raw string and any escape sequence inside it will be ignored.
"""

print r"This is \x04 \ngood example"
# Output
# This is \x04 \ngood example

"""
Format() method

Format strings contains curly braces {} as placeholders or replacement fields which gets replaced.

We can use positional arguments or keyword arguments to specify the order.

"""

# default(implicit) order
default_order = "{}, {} and {}".format('George', 'Alex', 'Thomas')
print '\n--- Default Order ---'
print default_order

# order using positional argument
positional_order = "{1}, {0} and {2}".format('George', 'Alex', 'Thomas')
print '\n--- Positional Order ---'
print positional_order

# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(g='George', a='Alex', t='Thomas')
print '\n--- Keyword Order ---'
print keyword_order

"""
Python String Methods
There are numerous methods available with the string object.

The format() method that we mentioned above is one of them.
Some of the commonly used methods are lower(), upper(), join(), split(), find(), replace() etc.

Here is a complete list of all the built-in methods to work with strings in Python.
"""

"OrgaNiC".lower()
# Output
# 'organic'

"OrgaNiC".upper()
# Output
# 'ORGANIC'

"This will split all words into a list".split()
# Output
# ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']

' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
# Output
# 'This will join all words into a string'

'Happy New Year'.find('ew')
# Output
# 7

'Happy New Year'.replace('Happy', 'Sad')
# Output
# 'Sad New Year'
