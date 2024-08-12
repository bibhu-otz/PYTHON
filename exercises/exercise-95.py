'''
 Write a Python program to check whether a string is numeric.
'''
# Define a string named str containing the value 'a123'.
str = 'a123'

# Uncomment the line below to test a different string (e.g., '123').
# str = '123'

# Try to convert the string str to a float.
try:
    i = float(str)
except (ValueError, TypeError):
    # If a ValueError or TypeError occurs during conversion, print 'Not numeric.'
    print('\nNot numeric')

# Print a newline character to format the output.
print()
