'''
Write a Python program to check whether a file exists.
'''
# Import the os.path module to work with file and directory paths.
import os.path

# Check if 'main.txt' is a file and print the result.
print(os.path.isfile('main.txt'))

# Check if 'main.py' is a file and print the result.
print(os.path.isfile('main.py'))
