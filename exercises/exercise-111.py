'''
Write a Python program to make file lists from the current directory using a wildcard.
'''
# Import the glob module, which allows you to search for files using wildcard patterns
import glob

# Use the glob module to get a list of all files in the current directory
file_list = glob.glob('*.*')

# Print the list of all files in the current directory
print(file_list)

# Specific files
# Use a wildcard pattern to search for Python (.py) files in the current directory
print(glob.glob('*.py'))

# Use a more specific pattern to search for files with names starting with a digit and any extension
print(glob.glob('./[0-9].*'))
