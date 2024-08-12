'''
 Write a Python program to find the path to a file or directory when you encounter a path name.
'''
# Prompt the user to input a number, and convert the input to a floating-point number.
num = float(input("Input a number: "))

# Check if the number is greater than zero.
if num > 0:
   # If true, print that it is a positive number.
   print("It is a positive number")
# Check if the number is equal to zero.
elif num == 0:
   # If true, print that it is zero.
   print("It is zero")
else:
   # If the above conditions are not met, print that it is a negative number.
   print("It is a negative number")
