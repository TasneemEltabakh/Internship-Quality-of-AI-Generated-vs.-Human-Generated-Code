# Python3 code to demonstrate working of
# Filter Range Length Tuples
# Using list comprehension + len()

# Initializing list
test_list = [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing desired lengths
i, j = 2, 3

# Filter Range Length Tuples
# Using list comprehension + len()
res = [sub for sub in test_list if len(sub) >= i and len(sub) <= j]

# printing result
print("The tuple list after filtering range records : " + str(res))