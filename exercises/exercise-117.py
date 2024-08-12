'''
Write a Python program to prove that two string variables of the same value point to the same memory location.
'''
# Define two string variables, str1 and str2, both containing the string "Python".
str1 = "Python"
str2 = "Python"
 
# Print the memory location (in hexadecimal) of str1 and str2 using the id() function.
print("\nMemory location of str1 =", hex(id(str1)))
print("Memory location of str2 =", hex(id(str2)))

# Print a blank line for separation.
print()
