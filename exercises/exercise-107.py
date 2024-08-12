'''
Write a Python program to retrieve file properties.
'''
# Import the 'os.path' and 'time' modules for working with file paths and time-related functions.
import os.path
import time
# Print the name of the current file using '__file__' attribute.
print('File         :', __file__)

# Print the access time of the current file using 'os.path.getatime()' and 'time.ctime()'.
print('Access time  :', time.ctime(os.path.getatime(__file__)))

# Print the modified time of the current file using 'os.path.getmtime()' and 'time.ctime()'.
print('Modified time:', time.ctime(os.path.getmtime(__file__)))

# Print the change time of the current file using 'os.path.getctime()' and 'time.ctime()'.
print('Change time  :', time.ctime(os.path.getctime(__file__)))

# Print the size of the current file using 'os.path.getsize()'.
print('Size         :', os.path.getsize(__file__))
