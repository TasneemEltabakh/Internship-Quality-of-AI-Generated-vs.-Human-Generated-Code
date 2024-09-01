# Python3 code to demonstrate working of
# Unique Tuple Frequency [ Order Irrespective ]
# Using tuple() + list comprehension + sorted() + len()

# initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Using tuple() + list comprehension + sorted() + len()
# Size computed after conversion to set
res = len(list(set(tuple(sorted(sub)) for sub in test_list)))

# printing result
print("Unique tuples Frequency : " + str(res))