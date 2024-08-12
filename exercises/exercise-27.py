'''
    Write a Python program that concatenates all elements 
    in a list into a string and returns it.
'''
# Define a function called concatenate_list_data that takes a list as a parameter.
def concatenate_list_data(lst):
    result = ''  # Initialize an empty string called result.
    
    # Iterate through the elements in the list.
    for element in lst:
        result += str(element)  # Convert each element to a string and concatenate it to the result.

    return result  # Return the concatenated string.

# Call the concatenate_list_data function with a list of numbers and print the result.
print(concatenate_list_data([1, 5, 12, 2]))
