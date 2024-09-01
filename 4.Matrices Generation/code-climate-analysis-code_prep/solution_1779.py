# Python3 code to demonstrate working of
# Tuple List intersection [ Order irrespective ]
# Using sorted() + set() + & operator + list comprehension

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Using sorted() + set() + & operator + list comprehension
# Using & operator to intersect, sorting before performing intersection
res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])

# printing result
print("List after intersection : " + str(res))