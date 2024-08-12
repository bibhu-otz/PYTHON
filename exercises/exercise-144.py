'''
 Write a Python program to check whether a variable is an integer or string.
'''
# Check if 25 is an instance of an integer (int) or a string (str).
print(isinstance(25, int) or isinstance(25, str))

# Check if the list containing 25 is an instance of an integer (int) or a string (str).
print(isinstance([25], int) or isinstance([25], str))

# Check if the string "25" is an instance of an integer (int) or a string (str).
print(isinstance("25", int) or isinstance("25", str))
