# Python3 code to demonstrate working of
# Row lengths counts
# Using dictionary + loop

# initializing list
test_list = [[6, 3, 1], [8, 9], [2],
[10, 12, 7], [4, 11]]

# printing original list
print("The original list is : " + str(test_list))

res = dict()
for sub in test_list:

# initializing incase of new length
if len(sub) not in res:
res[len(sub)] = 1

# increment in case of length present
else:
res[len(sub)] += 1

# printing result
print("Row length frequencies : " + str(res))