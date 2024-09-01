# import library
import re

# define a function
def find(string, sample) :

# check substring present
# in a string or not
if (sample in string):

y = "^" + sample

# check if string starts
# with the substring
x = re.search(y, string)

if x :
print("string starts with the given substring")

else :
print("string doesn't start with the given substring")

else :
print("entered string isn't a substring")


# Driver code
string = "geeks for geeks makes learning fun"
sample = "geeks"

# function call
find(string, sample)

sample = "makes"

# function call
find(string, sample)