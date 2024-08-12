'''
Write a Python program to extract the filename from a given path.
'''
# Import the 'os' module for operating system-related functions.
import os

# Print a newline for clarity.
print()

# Use 'os.path.basename' to extract the filename component from the given path.
# In this case, it extracts the filename 'homework-1.py' from the provided path.
print(os.path.basename('/users/system1/student1/homework-1.py'))

# Print another newline for clarity.
print()
