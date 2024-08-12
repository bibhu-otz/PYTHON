'''
Write a Python program that inputs a number and generates an error message if it is not a number.
'''
# Create an infinite loop using "while True."
while True:
    try:
        # Try to read an integer input from the user and store it in variable "a."
        a = int(input("Input a number: "))
        # If successful, break out of the loop and continue with the next code.
        break
    except ValueError:
        # If the input is not a valid integer, an exception (ValueError) is raised.
        # In that case, print an error message and prompt the user to try again.
        print("\nThis is not a number. Try again...")
        print()
