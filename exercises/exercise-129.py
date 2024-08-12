'''
 Write a Python program to add leading zeroes to a string.
'''
# Define the original string 'str1'.
str1 = '122.22'
print("Original String: ", str1)

# Print a message to indicate the purpose of the code.
print("\nAdded trailing zeros:")

# Use the 'ljust' method to add trailing zeros to 'str1' to make its total width 8.
str1 = str1.ljust(8, '0')
print(str1)

# Repeat the process to make the total width 10.
str1 = str1.ljust(10, '0')
print(str1)

# Print a message to indicate the addition of leading zeros.
print("\nAdded leading zeros:")

# Reset 'str1' to the original value.
str1 = '122.22'

# Use the 'rjust' method to add leading zeros to 'str1' to make its total width 8.
str1 = str1.rjust(8, '0')
print(str1)

# Repeat the process to make the total width 10.
str1 = str1.rjust(10, '0')
print(str1) 
