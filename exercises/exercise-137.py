'''
Write a Python program to extract a single key-value pair from a dictionary into variables.
'''
# Create a dictionary 'd' with a single key-value pair.
d = {'Red': 'Green'}

# Retrieve the items (key-value pairs) from the dictionary and unpack them into 'c1' and 'c2'.
# Note: Since 'd' contains only one key-value pair, we can safely unpack the items.
(c1, c2), = d.items()

# Print the first element, 'c1', which corresponds to the key 'Red'.
print(c1)

# Print the second element, 'c2', which corresponds to the value 'Green'.
print(c2)
