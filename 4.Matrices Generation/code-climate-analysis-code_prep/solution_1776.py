# Python3 code to demonstrate working of
# Convert tuple to List with succeeding element
# Using list comprehension


# initializing tuple
test_tup = (5, 6, 7, 4, 9)


# printing original tuple
print("The original tuple is : ", test_tup)


# initializing K
K = "Gfg"


# list comprehension for nested loop for flatten
res = [ele for sub in test_tup for ele in (sub, K)]


# printing result
print("Converted Tuple with K : ", res)