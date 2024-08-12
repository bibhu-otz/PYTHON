'''
Write a Python program to get the effective group id, effective user id, real group id, and a list of supplemental group ids associated with the current process.
'''
# Import the 'os' module for operating system-related functions.
import os

# Print a newline for clarity.
print()

# Get the effective group ID and print it.
print("Effective group id: ", os.getegid())

# Get the effective user ID and print it.
print("Effective user id: ", os.geteuid())

# Get the real group ID and print it.
print("Real group id: ", os.getgid())

# Get the list of supplemental group IDs and print them.
print("List of supplemental group ids: ", os.getgroups())

# Print another newline for clarity.
print()
