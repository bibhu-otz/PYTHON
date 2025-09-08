```
 Write a Python program to determine if a variable is defined or not.
```
# Try to execute a block of code.
try:
  x = 1
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")

# Try to execute another block of code that references an undefined variable.
try:
  y
except NameError:
  print("Variable is not defined....!")
else:
  print("Variable is defined.")
  
