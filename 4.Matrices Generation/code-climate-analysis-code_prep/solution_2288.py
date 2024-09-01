# Python3 code to demonstrate working of
# Skew Nested Tuple Summation
# Using infinite loop

# initializing tuple
test_tup = (5, (6, (1, (9, (10, None)))))

# printing original tuple
print("The original tuple is : " + str(test_tup))

res = 0
while test_tup:
res += test_tup[0]

# assigning inner tuple as original
test_tup = test_tup[1]

# printing result
print("Summation of 1st positions : " + str(res))