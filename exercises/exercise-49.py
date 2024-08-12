'''
Write a Python program to list all files in a directory.
'''
# Import necessary functions and modules from the 'os' library.
from os import listdir
from os.path import isfile, join

# Create a list 'files_list' that contains the names of files in the '/home/students' directory.
# It uses a list comprehension to filter files using 'isfile' and 'join' functions.
files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]

# Print the list of file names.
print(files_list)
