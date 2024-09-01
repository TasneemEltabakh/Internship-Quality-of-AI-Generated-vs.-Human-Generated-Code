# Python3 code to demonstrate working of
# Remove duplicate lists in tuples(Preserving Order)
# Using list comprehension + set()


# Initializing tuple
test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])


# printing original tuple
print("The original tuple is : " + str(test_tup))


# Remove duplicate lists in tuples(Preserving Order)
# Using list comprehension + set()
temp = set()
res = [ele for ele in test_tup if not(tuple(ele) in temp or temp.add(tuple(ele)))]


# printing result
print("The unique lists tuple is : " + str(res))