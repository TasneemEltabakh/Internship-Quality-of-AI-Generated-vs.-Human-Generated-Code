# Python3 code to demonstrate working of
# Remove K length Duplicates from String
# Using loop + slicing

# initializing strings
test_str = 'geeksforfreeksfo'

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 3

memo = set()
res = []
for idx in range(0, len(test_str) - K):

# slicing K length substrings
sub = test_str[idx : idx + K]

# checking for presence
if sub not in memo:
memo.add(sub)
res.append(sub)

res = ''.join(res[ele] for ele in range(0, len(res), K))

# printing result
print("The modified string : " + str(res))