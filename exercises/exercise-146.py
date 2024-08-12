'''
Write a Python program to find the location of Python module sources.
'''
# Import the 'imp' module, which provides access to the import-related functions.
import imp

# Print a message indicating the location of the Python 'os' module sources.
print("Location of Python os module sources:")

# Use the 'imp.find_module' function to find the location of the 'os' module sources and print the result.
print(imp.find_module('os'))

# Print a message indicating the location of the Python 'sys' module sources.
print("\nLocation of Python sys module sources:")

# Use the 'imp.find_module' function to find the location of the 'datetime' module sources and print the result.
print(imp.find_module('datetime'))
