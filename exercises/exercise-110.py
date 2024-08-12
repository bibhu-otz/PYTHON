'''
Write a  Python program to get numbers divisible by fifteen from a list using an anonymous function.
'''
# Create a list of numbers.
num_list = [45, 55, 60, 37, 100, 105, 220]

# Use an anonymous lambda function with the filter function to filter numbers in the list that are divisible by 15.
result = list(filter(lambda x: (x % 15 == 0), num_list))

# Print the numbers that are divisible by 15.
print("Numbers divisible by 15 are", result)
