# Python3 code to demonstrate working of
# Longest Substring of K
# Using loop

# initializing string
test_str = 'abcaaaacbbaa'

# printing original String
print("The original string is : " + str(test_str))

# initializing K
K = 'a'

cnt = 0
res = 0
for idx in range(len(test_str)):

# increment counter on checking
if test_str[idx] == K:
cnt += 1
else:
cnt = 0

# retaining max
res = max(res, cnt)

# printing result
print("The Longest Substring Length : " + str(res))