'''
Write a Python program to format a specified string and limit the length of a string.
'''
# Define a string containing a numeric value.
str_num = "1234567890"

# Print the original string.
print("Original string:", str_num)

# Print the first 6 characters of the string.
print('%.6s' % str_num)

# Print the first 9 characters of the string.
print('%.9s' % str_num)

# Print the entire string (first 10 characters) as it is.
print('%.10s' % str_num)
