'''
Write a Python program to filter positive numbers from a list.
'''
# Define a list named "nums" containing a series of integers.
nums = [34, 1, 0, -23, 12, -88]

# Print a message along with the original list of numbers.
print("Original numbers in the list: ", nums)

# Create a new list "new_nums" by using the "filter" function with a lambda function
# that filters out positive numbers from the "nums" list.
new_nums = list(filter(lambda x: x > 0, nums))

# Print a message along with the list of positive numbers from the "nums" list.
print("Positive numbers in the said list: ", new_nums)
