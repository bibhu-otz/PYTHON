'''
Write a Python program to calculate the time runs (difference between start and current time) of a program.
'''
# Import the 'default_timer' function from the 'timeit' module to measure elapsed time.
from timeit import default_timer
# Define a function 'timer' that takes an argument 'n'.
def timer(n):
    # Record the current time using the 'default_timer' function.
    start = default_timer()
   
    # Some code here (in this case, a loop to print numbers from 0 to 'n').
    for row in range(0, n):
        print(row)
    
    # Calculate the elapsed time by subtracting the start time from the current time,
    # and print the result.
    print(default_timer() - start)

# Call the 'timer' function with different values of 'n' to measure the execution time.
timer(5)
timer(15)
