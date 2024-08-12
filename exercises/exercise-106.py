'''
Write a Python program to divide a path by the extension separator.
'''
# Import the 'os.path' module for working with file paths.
import os.path
# Iterate through a list of example file paths.
for path in ['test.txt', 'filename', '/user/system/test.txt', '/', '']:
    # Print the file path and its corresponding file extension using 'os.path.splitext()'.
    print('"%s" :' % path, os.path.splitext(path))
