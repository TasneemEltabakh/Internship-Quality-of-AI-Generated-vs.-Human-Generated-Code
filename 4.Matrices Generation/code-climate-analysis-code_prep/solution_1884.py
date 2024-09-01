# Python3 code to demonstrate working of
# Convert Tuple Matrix to Tuple List
# Using list comprehension + zip()

# initializing list
test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

# printing original list
print("The original list is : " + str(test_list))

# flattening
temp = [ele for sub in test_list for ele in sub]

# joining to form column pairs
res = list(zip(*temp))

# printing result
print("The converted tuple list : " + str(res))