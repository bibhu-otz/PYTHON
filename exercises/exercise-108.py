'''
Write a Python program to find the path to a file or directory when you encounter a path name.
'''
# Import the 'os.path' module for working with file paths.
import os.path
# Iterate through a list of file paths, including '__file__', the directory of '__file__', '/', and a broken link.
for file in [__file__, os.path.dirname(__file__), '/', './broken_link']:
    # Print the name of the current file.
    print('File        :', file)

    # Check if the file path is an absolute path using 'os.path.isabs()'.
    print('Absolute    :', os.path.isabs(file))

    # Check if the file path points to an existing file using 'os.path.isfile()'.
    print('Is File?    :', os.path.isfile(file))

    # Check if the file path points to an existing directory using 'os.path.isdir()'.
    print('Is Dir?     :', os.path.isdir(file))

    # Check if the file path is a symbolic link using 'os.path.islink()'.
    print('Is Link?    :', os.path.islink(file))

    # Check if the file path exists (regardless of its type) using 'os.path.exists()'.
    print('Exists?     :', os.path.exists(file))

    # Check if the symbolic link exists using 'os.path.lexists()'.
    print('Link Exists?:', os.path.lexists(file))
