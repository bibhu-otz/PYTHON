'''
    Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
    Sample data : 3, 5, 7, 23
    Output :
    List : ['3', ' 5', ' 7', ' 23']
    Tuple : ('3', ' 5', ' 7', ' 23')
'''
# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
values = input("Input some comma-separated numbers: ")

# Split the 'values' string into a list using commas as separators and store it in the 'list' variable
list = values.split(",")

# Convert the 'list' into a tuple and store it in the 'tuple' variable
tuple = tuple(list)

# Print the list
print('List : ', list)

# Print the tuple
print('Tuple : ', tuple)