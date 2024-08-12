'''
 Write a Python program to retrieve the path and name of the file currently being executed.
'''
# Import the 'os' module to work with the operating system.
import os
# Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
# This will print the path of the current file.
print("Current File Name: ", os.path.realpath(__file__))
