# Python program to list out
# all the empty directories


import os

# List to store all empty
# directories
empty = []

# Traversing through Test
for root, dirs, files in os.walk('Test'):

# Checking the size of tuple
if not len(dirs) and not len(files):

# Adding the empty directory to
# list
empty.append(root)

Print("Empty Directories:")
print(empty)