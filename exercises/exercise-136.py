'''
Write a Python program to find files and skip directories in a given directory.
'''
# Import the 'os' module to work with the operating system.
import os

# Use a list comprehension to generate a list of files in the '/home/students' directory.
# For each 'f' (file or folder name) in the list of entries in '/home/students':
# - Use 'os.path.join' to construct an absolute path to the entry.
# - Check if the constructed path represents a file using 'os.path.isfile'.
# - Include 'f' in the list if it's a file.

# Print the list of files.
print([f for f in os.listdir('/home/students') if os.path.isfile(os.path.join('/home/students', f))])
