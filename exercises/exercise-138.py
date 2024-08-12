'''
 Write a Python program to convert true to 1 and false to 0.
'''
# Set the variable 'x' to the string 'true'.
x = 'true'

# Use the comparison 'x == 'true'' to check if 'x' is equal to the string 'true'. 
# The result of this comparison will be either True or False.

# Convert the result (True or False) into an integer (1 or 0) using the 'int()' function.
x = int(x == 'true')

# Print the value of 'x' after conversion. 
# If 'x' was 'true', it will be converted to 1 (True), and if 'x' was not 'true', it will be converted to 0 (False).
print(x)

# Set the variable 'x' to the string 'abcd'.
x = 'abcd'

# Repeat the same process: Use the comparison 'x == 'true'' to check if 'x' is equal to the string 'true'. 
# Convert the result (True or False) into an integer (1 or 0) using the 'int()' function.
x = int(x == 'true')

# Print the value of 'x' after conversion. 
# Since 'x' was not 'true', it will be converted to 0 (False).
print(x)
