'''
Write a Python program to get the details of the math module.
'''
# Imports the math module
import math            
# Use the 'dir' function to get a list of names in the 'math' module, including functions and constants.
# Store this list in the 'math_ls' variable.
math_ls = dir(math)
# Print the list of names in the 'math' module, which includes mathematical functions and constants.
print(math_ls)
