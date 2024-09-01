# Python3 code to demonstrate working of
# Elements frequency in Tuple
# Using defaultdict()
from collections import defaultdict


# initializing tuple
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)


# printing original tuple
print("The original tuple is : " + str(test_tup))


res = defaultdict(int)
for ele in test_tup:

# incrementing frequency
res[ele] += 1


# printing result
print("Tuple elements frequency is : " + str(dict(res)))