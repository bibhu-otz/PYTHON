'''
Write a Python function to check whether a number is divisible by another number. Accept two integer values from the user.
'''
# Define a function named 'multiple' that takes two arguments, 'm' and 'n'.
def multiple(m, n):
    # Check if 'm' is a multiple of 'n' by using the modulo operator.
    # If the remainder is 0, return True, indicating 'm' is a multiple of 'n'.
    # Otherwise, return False.
    return True if m % n == 0 else False

# Call the 'multiple' function with different arguments and print the results.
print(multiple(20, 5))  # Check if 20 is a multiple of 5 and print the result.
print(multiple(7, 2))   # Check if 7 is a multiple of 2 and print the result.
