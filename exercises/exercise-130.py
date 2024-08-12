'''
Write a  Python program that uses double quotes to display strings.
'''
# Import the 'json' module to work with JSON data.
import json
# Create a Python dictionary with key-value pairs.
data = {'Alex': 1, 'Suresh': 2, 'Agnessa': 3}

# Use the 'json.dumps()' function to convert the dictionary to a JSON-formatted string and print it.
json_string = json.dumps(data)
print(json_string)
