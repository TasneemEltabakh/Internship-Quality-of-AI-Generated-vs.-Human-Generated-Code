# Python3 code to demonstrate working of
# Consecutive characters frequency
# Using list comprehension + groupby()
from itertools import groupby

# initializing string
test_str = "geekksforgggeeks"

# printing original string
print("The original string is : " + test_str)

# Consecutive characters frequency
# Using list comprehension + groupby()
res = [len(list(j)) for _, j in groupby(test_str)]

# printing result
print("The Consecutive characters frequency : " + str(res))