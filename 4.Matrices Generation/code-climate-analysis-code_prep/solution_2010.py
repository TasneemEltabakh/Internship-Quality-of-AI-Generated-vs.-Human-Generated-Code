# Python3 code to demonstrate working of
# Cross Pairing in Tuple List
# Using list comprehension

# initializing lists
test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# corresponding loop in list comprehension
res = [(sub1[1], sub2[1]) for sub2 in test_list2 for sub1 in test_list1 if sub1[0] == sub2[0]]

# printing result
print("The mapped tuples : " + str(res))