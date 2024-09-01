# Import required module
import re


# Function to depict use of finditer() method
def CntSubstr(pattern, string):

# Array storing the indices
a = [m.start() for m in re.finditer(pattern, string)]
return a


# Driver Code
string = 'geeksforgeeksforgeeks'
pattern = 'geeksforgeeks'

# Printing index values of non-overlapping pattern
print(CntSubstr(pattern, string))