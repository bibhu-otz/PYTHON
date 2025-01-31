'''
Write a Python program that determines whether a given number 
(accepted from the user) 
is even or odd, and prints an appropriate message to the user.
'''
# Prompt the user to enter a number and convert the input to an integer
num = int(input('enter a number'))

# Calculate the remainder when the number is divided by 2
mod = num % 2

# Check if the remainder is greater than 0, indicating an odd number
if mod > 0:
    # Print a message indicating that the number is odd
    print("This is an odd number.")
else:
    # Print a message indicating that the number is even
    print("This is an even number.")
