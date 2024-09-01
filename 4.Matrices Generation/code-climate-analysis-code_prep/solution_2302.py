# Python3 code to demonstrate working of
# Frequency of numbers in String
# Using re.findall() + len()
import re

# initializing string
test_str = "geeks4feeks is No. 1 4 geeks"

# printing original string
print("The original string is : " + test_str)

# Frequency of numbers in String
# Using re.findall() + len()
res = len(re.findall(r'\d+', test_str))

# printing result
print("Count of numerics in string : " + str(res))