# Python3 code to demonstrate working of
# Tuple XOR operation
# using zip() + generator expression

# initialize tuples
test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Tuple XOR operation
# using zip() + generator expression
res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))

# printing result
print("The XOR tuple : " + str(res))