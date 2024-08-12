'''
Write a Python program that calls an external command.
'''
# Import the 'call' function from the 'subprocess' module.
from subprocess import call

# Use the 'call' function to execute the "ls -l" command.
# This command lists the files and directories in the current directory with details.
call(["ls", "-l"])
