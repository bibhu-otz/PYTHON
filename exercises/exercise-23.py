'''
Write a Python program to get n (non-negative integer) 
copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is 
less than 2.
'''
# Define a function called substring_copy that takes two parameters: text (a string) and n (an integer).
def substring_copy(text, n):
  # Set the initial value of flen (substring length) to 2.
  flen = 2

  # Check if flen is greater than the length of the input text.
  if flen > len(text):
    # If flen is greater, set it to the length of the text to avoid going out of bounds.
    flen = len(text)

  # Extract a substring of length flen from the beginning of the text.
  substr = text[:flen]

  # Initialize an empty string result to store the concatenated substrings.
  result = ""

  # Iterate n times to concatenate the substring to the result.
  for i in range(n):
    result = result + substr

  # Return the final result after concatenating substrings.
  return result

# Call the substring_copy function with two different inputs and print the results.
print(substring_copy('abcdef', 2))  # Output: "abab" (substring "ab" repeated 2 times)
print(substring_copy('p', 3))  # Output: "pp" (substring "p" repeated 3 times)
