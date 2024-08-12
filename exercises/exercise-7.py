'''
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''
file_name = input('Enter a file name with extension')

file_ext  = file_name.split('.')
print(file_ext)
print("The extension of the file is : " + file_ext[-1])
print("The extension of the file is : " + repr(file_ext[-1]))