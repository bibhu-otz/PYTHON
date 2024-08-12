'''
Write a  Python program to locate Python site packages.
'''
# Import the 'site' module.
import site

# Use the 'site.getsitepackages()' function to retrieve site packages' paths.
# 'site.getsitepackages()' returns a list of paths where site packages are installed.
print(site.getsitepackages())
