# Python3 code to demonstrate working of
# Sort dictionaries list by Key's Value list index
# Using sorted() + lambda

# initializing lists
test_list = [{"Gfg" : [6, 7, 8], "is" : 9, "best" : 10},
{"Gfg" : [2, 0, 3], "is" : 11, "best" : 19},
{"Gfg" : [4, 6, 9], "is" : 16, "best" : 1}]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = "Gfg"

# initializing idx
idx = 2

# using sorted() to perform sort in basis of 1 parameter key and
# index
res = sorted(test_list, key = lambda ele: ele[K][idx])

# printing result
print("The required sort order : " + str(res))