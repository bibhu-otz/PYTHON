'''
Write a Python program to count the number 4 in a given list.
'''
# Define a function called list_count_4 that takes a list of numbers (nums) as a parameter.
def list_count_4(nums):
  # Initialize a variable count to keep track of the count of occurrences of the number 4.
  count = 0

  # Iterate through each element (num) in the input list (nums).
  for num in nums:
    # Check if the current element (num) is equal to 4.
    if num == 4:
      # If the element is 4, increment the count by 1.
      count = count + 1

  # Return the final count after iterating through the list.
  return count

# Call the list_count_4 function with two different input lists and print the results.
print(list_count_4([1, 4, 6, 7, 4]))  # Output: 2 (There are two occurrences of 4 in the list.)
print(list_count_4([1, 4, 6, 4, 7, 4]))  # Output: 3 (There are three occurrences of 4 in the list.)
