import decimal

'''
Floating-point numbers are implemented in computer hardware as binary fractions, as computer
only understands binary (0 and 1). Due to this reason, most of the decimal fractions we know,
cannot be accurately stored in our computer.
'''


# Output false
(1.1 + 2.2) == 3.3
'''
Fractional 1/3 as a decimal number. This will give 0.33333333... which is infinitely long, and can
only be approximated.

Decimal fraction 0.1 will result into an infinitely long binary fraction of 0.000110011001100110011...
and a computer will only store a finite number of it.

This will only approximate 0.1 but never be equal. Hence, it is the limitation of our computer
hardware and not an error in Python.
'''

# Proof
1.1 + 2.2
# Output 3.3000000000000003

'''
To overcome this issue, we can use decimal module. While floating point numbers have precision
up to 15 decimal places, the decimal module has user settable precision.
'''

# Output: 0.1
print(0.1)

# Output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal(0.1))

'''
Decimal module also preserves significance as exhibited by the examples below:
'''
# Output: Decimal('3.3')
print(decimal.Decimal('1.1') + decimal.Decimal('2.2'))

# Output: Decimal('3.000')
print(decimal.Decimal('1.2') * decimal.Decimal('2.50'))
