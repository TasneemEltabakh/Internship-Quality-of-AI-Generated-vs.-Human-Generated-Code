# Python3 code to demonstrate working of
# Extract elements with Frequency greater than K
# Using count() + loop

# initializing list
test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# printing string
print("The original list : " + str(test_list))

# initializing K
K = 2

res = []
for i in test_list:

# using count() to get count of elements
freq = test_list.count(i)

# checking if not already entered in results
if freq > K and i not in res:
res.append(i)

# printing results
print("The required elements : " + str(res))