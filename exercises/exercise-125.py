'''
 Write a Python program to sum all counts in a collection.
'''
# Import the 'collections' module, which provides the 'Counter' class.
import collections

# Define a list of numbers.
num = [2, 2, 4, 6, 6, 8, 6, 10, 4]

# Use 'collections.Counter' to count the occurrences of each number and sum the values.
# 'collections.Counter' returns a dictionary-like object with elements as keys and their counts as values.
# 'sum(collections.Counter(num).values())' calculates the sum of these counts.
result = sum(collections.Counter(num).values())

# Print the result, which is the sum of the counts.
print(result)
