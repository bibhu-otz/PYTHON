'''
 Write a Python program to convert an integer to binary that keeps leading zeros.
'''
# Define an integer variable 'x' with the value 12.
x = 12
# Print the binary representation of 'x' with leading zeros.
# The 'format' function is used with the format specifier '08b' to format 'x' as an 8-character binary string.
# It ensures that there are leading zeros to make it 8 characters long.
print(format(x, '08b'))
# Print the binary representation of 'x' with leading zeros.
# The 'format' function is used with the format specifier '010b' to format 'x' as a 10-character binary string.
# It ensures that there are leading zeros to make it 10 characters long.
print(format(x, '010b'))
