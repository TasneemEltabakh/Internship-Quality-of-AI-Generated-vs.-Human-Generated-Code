# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + lambda

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using map() + lambda
res = tuple(map(lambda i, j: i & j, test_tup1, test_tup2))

# printing result
print("Resultant tuple after AND operation : " + str(res))