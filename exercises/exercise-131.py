'''
Write a Python program to split a variable length string into variables.
'''
# Create a list of variables 'x', 'y', and 'z'.
var_list = ['a', 'b', 'c']

# Assign the first three elements of 'var_list' to 'x', 'y', and 'z'. Use [None] * 3 to ensure enough elements are available.
x, y, z = (var_list + [None] * 3)[:3]

# Print the values of 'x', 'y', and 'z'.
print(x, y, z)

# Create a new list of variables 'x' and 'y'.
var_list = [100, 20.25]

# Assign the first two elements of 'var_list' to 'x' and 'y'. Use [None] * 2 to ensure enough elements are available.
x, y = (var_list + [None] * 2)[:2]

# Print the values of 'x' and 'y'.
print(x, y)
