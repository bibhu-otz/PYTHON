'''
Write a Python program to check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones of same length in a given string. Return True/False.
'''
# Define a function 'test' that checks if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in a string 'str1'.
def test(str1):
    # Use a 'while' loop to repeatedly find and replace '01' with an empty string in 'str1'.
    while '01' in str1:
        str1 = str1.replace('01', '')
    
    # Check if the length of the modified 'str1' is equal to 0 and return the result.
    return len(str1) == 0

# Define the input string 'str1'.
str1 = "01010101"

# Print the original sequence.
print("Original sequence:", str1)

# Print the result of the 'test' function for 'str1'.
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))

# Repeat the same process for other test cases.
str1 = "00"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "000111000111"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
str1 = "00011100011"
print("\nOriginal sequence:", str1)
print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
print(test(str1))
