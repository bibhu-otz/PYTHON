'''
Write a Python program to compute the product of a list of integers (without using a for loop).
'''
# Import the 'reduce' function from the 'functools' module.
from functools import reduce

# Define a list named 'nums' containing a series of integers.
nums = [10, 20, 30]

# Print a message along with the original list of numbers.
print("Original list numbers:")
print(nums)

# Calculate the product of the numbers in the list 'nums' using the 'reduce' function
# and a lambda function that multiplies two numbers.
nums_product = reduce((lambda x, y: x * y), nums)

# Print the product of the numbers, obtained without using a for loop.
print("\nProduct of the said numbers (without using a for loop):", nums_product)
