'''
Write a Python program to get the execution time of a Python method.
'''
# Import the 'time' module to work with time-related functions.
import time

# Define a function named 'sum_of_n_numbers' that calculates the sum of the first 'n' natural numbers.
def sum_of_n_numbers(n):
    # Record the current time before the calculation.
    start_time = time.time()

    # Initialize a variable 's' to store the sum.
    s = 0

    # Loop through numbers from 1 to 'n' and accumulate the sum.
    for i in range(1, n + 1):
        s = s + i

    # Record the current time after the calculation.
    end_time = time.time()

    # Return both the calculated sum and the time taken for the calculation.
    return s, end_time - start_time

# Define the value of 'n' as 5.
n = 5

# Print the result, including the time taken to calculate the sum.
print("\nTime to sum of 1 to", n, "and required time to calculate is:", sum_of_n_numbers(n))
