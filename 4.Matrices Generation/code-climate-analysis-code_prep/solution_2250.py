# Python3 code to demonstrate working of
# Filter Strings combination of K substrings
# Using permutations() + map() + join() + set() + loop
from itertools import permutations

# initializing list
test_list = ["geeks4u", "allbest", "abcdef"]

# printing string
print("The original list : " + str(test_list))

# initializing substring list
substr_list = ["s4u", "est", "al", "ge", "ek", "def", "lb"]

# initializing K
K = 3

# getting all permutations
perms = list(set(map(''.join, permutations(substr_list, r = K))))

# using loop to check permutations with list
res = []
for ele in perms:
if ele in test_list:
res.append(ele)

# printing results
print("Strings after joins : " + str(res))