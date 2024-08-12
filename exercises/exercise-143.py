'''
Write a  Python program to determine if the Python shell is executing in 32-bit or 64-bit mode on the operating system.
'''
# Import the 'struct' module for working with C-style data in Python.
import struct
# Use 'struct.calcsize("P")' to calculate the size of a C 'void *' pointer in bytes and 'struct.calcsize("P") * 8' to convert it to bits.

# Print the result, which represents the size of a C 'void *' pointer in bits.
print(struct.calcsize("P") * 8)
