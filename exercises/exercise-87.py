'''
 Write a Python program to get the size of a file.
'''
# Import the os module for file operations.
import os
# Get the size of the file "abc.txt".
file_size = os.path.getsize("abc.txt")
# Print the size of the file "abc.txt" in bytes.
print("\nThe size of abc.txt is:", file_size, "Bytes")
# Print a newline character for spacing.
print()
