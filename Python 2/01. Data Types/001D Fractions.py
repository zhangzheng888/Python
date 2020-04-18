import fractions

'''
Data Types: Numbers (Python 2.7)

Fractions

Python provides operations involving fractional numbers through its fractions module.

A fraction has a numerator and a denominator, both of which are integers. This module has support
for rational number arithmetic.
'''

# Output: 3/2
print fractions.Fraction(1.5)

# Output: 4
print fractions.Fraction(4)

# Output: 1/7
print fractions.Fraction(1, 7)

# Fraction from float, may yield unusual results
# As float
# Output: 2476979795053773/2251799813685248
print fractions.Fraction(1.1)

# Fraction allows instantiation from string
# As string
# Output: 11/10
print fractions.Fraction('1.1')

# Output: 1/3
print fractions.Fraction(1, 6) + fractions.Fraction(1, 6)

# Output: 8/5
print 1 / fractions.Fraction(5, 8)

# Output: False
print fractions.Fraction(-5, 10) > 0

# Output: True
print fractions.Fraction(-5, 10) < 0
