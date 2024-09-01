# Python3 code to demonstrate working of
# Values Associated Keys
# Using defaultdict() + loop
from collections import defaultdict

# initializing dictionary
test_dict = {'gfg' : [1, 2, 3], 'is' : [1, 4], 'best' : [4, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Values Associated Keys
# Using defaultdict() + loop
res = defaultdict(list)
for key, val in test_dict.items():
for ele in val:
res[ele].append(key)

# printing result
print("The values associated dictionary : " + str(dict(res)))