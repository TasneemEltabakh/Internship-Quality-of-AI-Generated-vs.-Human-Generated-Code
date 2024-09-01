# Python3 code to demonstrate working of
# Adjacent element multiplication
# using zip() + generator expression + tuple

# initialize tuple
test_tup = (1, 5, 7, 8, 10)

# printing original tuple
print("The original tuple : " + str(test_tup))

# Adjacent element multiplication
# using zip() + generator expression + tuple
res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))

# printing result
print("Resultant tuple after multiplication : " + str(res))