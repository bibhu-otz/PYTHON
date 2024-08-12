'''
Write a Python program to get a directory listing, sorted by creation date.
'''
# Import necessary modules: 'stat' for file status, 'os' for operating system interactions,
# 'sys' for command-line arguments, and 'time' for time-related functions.
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
# Determine the directory path based on command-line arguments. If there are two arguments, use the second one as the path; otherwise, use the current directory.
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
# Generate a generator expression that yields the full path for each file in the specified directory.
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
# Generate a generator expression that pairs the file's status information and its path.
data = ((os.stat(path), path) for path in data)
# Filter the files to keep only regular files (S_ISREG) and extract their creation times (ST_CTIME).
data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))
# Sort the files based on their creation times and then print the sorted list, including the creation time and the file name.
for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path)) 
