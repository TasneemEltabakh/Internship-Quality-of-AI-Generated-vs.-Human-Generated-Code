# import from string all ascii_lowercase and asc_lower
from string import ascii_lowercase as asc_lower


# function to check if all elements are present or not
def check(s):
return set(asc_lower) - set(s.lower()) == set([])

# driver code
string ="The quick brown fox jumps over the lazy dog"
if(check(string)== True):
print("The string is a pangram")
else:
print("The string isn't a pangram")