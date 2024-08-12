'''
Write a Python program to check whether lowercase letters exist in a string.
'''
# Assign the string 'A8238i823acdeOUEI' to the variable 'str1'.
str1 = 'A8238i823acdeOUEI'

# Check if there is any lowercase character in the string 'str1'.
# The 'any' function returns True if at least one character is lowercase.
print(any(c.islower() for c in str1))
