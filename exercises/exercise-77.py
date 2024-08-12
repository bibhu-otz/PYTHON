'''
 Write a  Python program to test whether the system is a big-endian platform or a little-endian platform.
'''
# Import the sys module to access system-specific information.
import sys

# Display a blank line for clarity.
print()

# Check if the byte order of the platform is "little" (e.g., Intel, Alpha) and display a corresponding message.
if sys.byteorder == "little":
    print("Little-endian platform.")
else:
    # If the byte order is not "little," assume it's "big" (e.g., Motorola, SPARC) and display a corresponding message.
    print("Big-endian platform.")

# Display another blank line for clarity.
print()
