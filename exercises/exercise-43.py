'''
Write a Python program to get OS name, platform and release information.
'''
# Import the 'platform' and 'os' modules.
import platform
import os

# Print the name of the operating system based on the 'os.name' attribute.
# 'os.name' provides the name of the operating system dependent module imported.
print("Name of the operating system:", os.name)

# Print the name of the OS system using the 'platform.system()' function.
# 'platform.system()' returns the name of the operating system, such as 'Windows', 'Linux', or 'Darwin' (macOS).
print("\nName of the OS system:", platform.system())

# Print the version of the operating system using the 'platform.release()' function.
# 'platform.release()' returns the version or release of the operating system.
print("\nVersion of the operating system:", platform.release())
