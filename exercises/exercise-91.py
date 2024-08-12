'''
 Write a  Python program to swap two variables.
'''
# Initialize two variables 'a' and 'b' with values 30 and 20, respectively.
a = 30
b = 20
# Print the values of 'a' and 'b' before swapping, using string formatting.
print("\nBefore swap a = %d and b = %d" %(a, b))
# Swap the values of 'a' and 'b' using a tuple assignment. This line effectively swaps the values.
a, b = b, a
# Print the values of 'a' and 'b' after swapping, using string formatting.
print("\nAfter swaping a = %d and b = %d" %(a, b))
