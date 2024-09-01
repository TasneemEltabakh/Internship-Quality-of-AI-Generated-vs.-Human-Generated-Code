# Python3 code to demonstrate working of
# Convert Tuple to Tuple Pair
# Using product() + next()
from itertools import product

# initializing tuple
test_tuple = ('G', 'F', 'G')

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Convert Tuple to Tuple Pair
# Using product() + next()
test_tuple = iter(test_tuple)
res = list(product(next(test_tuple), test_tuple))

# printing result
print("The paired records : " + str(res))