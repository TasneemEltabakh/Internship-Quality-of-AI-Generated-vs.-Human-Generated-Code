# Python3 code to demonstrate working of
# Consecutive Kth column Difference in Tuple List
# Using loop

# initializing list
test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

res = []
for idx in range(0, len(test_list) - 1):

# getting difference using abs()
res.append(abs(test_list[idx][K] - test_list[idx + 1][K]))

# printing result
print("Resultant tuple list : " + str(res))