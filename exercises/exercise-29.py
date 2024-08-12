'''
    Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
    Test Data :
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    Expected Output :
    {'Black', 'White'}
'''
# Create two sets, color_list_1 and color_list_2.
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# Print the original elements of the sets.
print("Original set elements:")
print(color_list_1)
print(color_list_2)

# Calculate and print the difference of color_list_1 and color_list_2.
print("\nDifference of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))

# Calculate and print the difference of color_list_2 and color_list_1.
print("\nDifference of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
