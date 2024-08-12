'''
Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.
'''
# Define a function named "sum_thrice" that takes three integer parameters: x, y, and z
def sum_thrice(x, y, z):
    # Calculate the sum of x, y, and z
    sum = x + y + z

    # Check if x, y, and z are all equal (all three numbers are the same)
    if x == y == z:
        # If they are equal, triple the sum
        sum = sum * 3

    # Return the final sum
    return sum

# Call the "sum_thrice" function with the arguments (1, 2, 3) and print the result
print(sum_thrice(1, 2, 3))

# Call the "sum_thrice" function with the arguments (3, 3, 3) and print the result
print(sum_thrice(3, 3, 3))
