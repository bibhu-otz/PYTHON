'''
Write a Python program to get an absolute file path.
''' 
# Define a function named absolute_file_path that takes a parameter 'path_fname'.
def absolute_file_path(path_fname):
    # Import the 'os' module for working with file paths and directories.
    import os
    
    # Use 'os.path.abspath()' to get the absolute file path by providing 'path_fname'.
    return os.path.abspath(path_fname)

# Call the function and print the result, passing "test.txt" as the argument.
print("Absolute file path: ", absolute_file_path("test.txt"))
