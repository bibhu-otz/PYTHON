'''
Write a Python program to determine the largest and smallest integers, longs, and floats.
'''
# Import the sys module to access system-related information.
import sys

# Print information about the float data type.
print("Float value information: ", sys.float_info)

# Print information about the integer data type (Note: there is no sys.int_info, this is incorrect).
print("\nInteger value information: ", sys.int_info)

# Print the maximum size of an integer that can be represented on the current system.
print("\nMaximum size of an integer: ", sys.maxsize)
