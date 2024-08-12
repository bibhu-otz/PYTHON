'''
Write a Python program to check whether an integer fits in 64 bits.
'''
# Assign the integer value 30 to the variable 'int_val'.
int_val = 30

# Check if the bit length of 'int_val' is less than or equal to 63.
if int_val.bit_length() <= 63:
    # Print the bit length of the minimum 64-bit signed integer (-2^63).
    print((-2 ** 63).bit_length())

    # Print the bit length of the maximum 64-bit signed integer (2^63 - 1).
    print((2 ** 63).bit_length())
