# Python3 code to demonstrate working of
# Remove None Tuples from List
# Using all() + list comprehension

# initializing list
test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]

# printing original list
print("The original list is : " + str(test_list))

# negating result for discarding all None Tuples
res = [sub for sub in test_list if not all(ele == None for ele in sub)]

# printing result
print("Removed None Tuples : " + str(res))