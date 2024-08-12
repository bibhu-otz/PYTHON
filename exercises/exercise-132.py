'''
Write a Python program to list the home directory without an absolute path.
'''
# Import the 'os.path' module to work with file paths and directories.
import os.path
# Use the 'os.path.expanduser()' function to expand the '~' character to the user's home directory.
# It returns the absolute path to the user's home directory.
print(os.path.expanduser('~'))
