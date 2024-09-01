# Python3 code to demonstrate working of
# Group Elements in Matrix
# Using dictionary comprehension + loop

# initializing list
test_list = [[5, 8], [2, 0], [5, 4], [2, 3], [7, 9]]

# printing original list
print("The original list : " + str(test_list))

# initializing empty dictionary with default empty list
res = {idx[0]: [] for idx in test_list}

# using loop for grouping
for idx in test_list:
res[idx[0]].append(idx[1])

# printing result
print("The Grouped Matrix : " + str(res))