'''
Write a Python program to get the actual module object for a given object.
'''
# Import the 'getmodule' function from the 'inspect' module.
from inspect import getmodule

# Import the 'sqrt' function from the 'math' module.
from math import sqrt

# Use the 'getmodule' function to get the module where the 'sqrt' function is defined.
# Then, print the module information for the 'sqrt' function.
print(getmodule(sqrt))
