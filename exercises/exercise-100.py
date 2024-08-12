'''
Write a Python program to get the name of the host on which the routine is running.
'''
# Import the 'socket' module to work with networking functionalities.

import socket
# Use 'socket.gethostname()' to retrieve the name of the current host or machine.
host_name = socket.gethostname()

# Print the host name to the console.
print("Host name:", host_name)
