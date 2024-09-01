# Python3 code to demonstrate working of
# Intersection in Tuple Records Data
# Using list comprehension

# Initializing lists
test_list1 = [('gfg', 1), ('is', 2), ('best', 3)]
test_list2 = [('i', 3), ('love', 4), ('gfg', 1)]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Intersection in Tuple Records Data
# Using list comprehension
res = [ele1 for ele1 in test_list1
for ele2 in test_list2 if ele1 == ele2]

# printing result
print("The Intersection of data records is : " + str(res))