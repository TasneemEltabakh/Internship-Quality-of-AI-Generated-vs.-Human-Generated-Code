# Python3 code to demonstrate working of
# Split String on vowels
# Using split() + regex
import re


# initializing strings
test_str = 'GFGaBste4oCS'


# printing original string
print("The original string is : " + str(test_str))


# splitting on vowels
# constructing vowels list
# and separating using | operator
res = re.split('a|e|i|o|u', test_str)


# printing result
print("The splitted string : " + str(res))