'''
Write a Python program to input two integers on a single line.
'''
# Print a message to instruct the user to input the values of 'x' and 'y'.
print("Input the value of x & y")

# Use 'map' to apply the 'int' function to the input values and split them into variables 'x' and 'y'.
x, y = map(int, input().split())

# Print the values of 'x' and 'y' after they have been assigned.
print("The value of x & y are: ", x, y)
