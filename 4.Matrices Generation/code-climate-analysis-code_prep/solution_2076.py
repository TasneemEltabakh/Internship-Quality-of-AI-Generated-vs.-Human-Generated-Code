# Python3 code to demonstrate working of
# Sort lists in tuple
# Using tuple() + sorted() + generator expression

# Initializing tuple
test_tup = ([7, 5, 4], [8, 2, 4], [0, 7, 5])

# printing original tuple
print("The original tuple is : " + str(test_tup))

# Sort lists in tuple
# Using tuple() + sorted() + generator expression
res = tuple((sorted(sub) for sub in test_tup))

# printing result
print("The tuple after sorting lists : " + str(res))