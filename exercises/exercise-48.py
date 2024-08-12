'''
Write a Python program to parse a string to float or integer
'''
# Define a string 'n' containing a numeric value.
n = "246.2458"

# Convert the string 'n' to a floating-point number and print the result.
print(float(n))

# Convert the floating-point number to an integer, truncating any decimal part, and print the result.
print(int(float(n)))
