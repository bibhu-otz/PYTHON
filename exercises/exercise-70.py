'''
Write a Python program to sort files by date.
'''
# Import the necessary libraries to work with file operations and globbing.
import glob
import os

# Use the glob module to find all files in the current directory with a ".txt" extension.
files = glob.glob("*.txt")

# Sort the list of file names based on the modification time (getmtime) of each file.
files.sort(key=os.path.getmtime)

# Print the sorted list of file names, one per line.
print("\n".join(files))
