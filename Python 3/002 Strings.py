"""
Data Types: Strings

A string is a sequence of characters.

A string is a sequence of characters. Computers do not deal with characters, they deal with numbers
 (binary). Even though you may see characters on your screen, internally it is stored and
 manipulated as a combination of 0's and 1's.

A character is simply a symbol. This conversion of character to a number is called encoding, and
the reverse process is decoding. ASCII and Unicode are some of the popular encoding used.

Strings are used in Python to record text information, such as names.

Strings in Python are actually a sequence, which basically means Python keeps track of every e
lement in the string as a sequence. This idea of a sequence is an important one in Python and we
will touch upon in more detail in the Strings Accessibility.
"""

# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
