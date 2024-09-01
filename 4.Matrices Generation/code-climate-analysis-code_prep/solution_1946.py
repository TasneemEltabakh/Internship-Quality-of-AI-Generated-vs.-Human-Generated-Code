# import library
import re

# list of different types of file
filenames = ["gfg.html", "geeks.xml",
"computer.txt", "geeksforgeeks.jpg"]

for file in filenames:
# search given pattern in the line
match = re.search("\.xml$", file)

# if match is found
if match:
print("The file ending with .xml is:",
file)