# Python3 code to demonstrate working of
# Custom sorting in list of tuples
# Using sorted() + lambda

# Initializing list
test_list = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]

# printing original list
print("The original list is : " + str(test_list))

# Custom sorting in list of tuples
# Using sorted() + lambda
res = sorted(test_list, key = lambda sub: (-sub[0], sub[1]))

# printing result
print("The tuple after custom sorting is : " + str(res))