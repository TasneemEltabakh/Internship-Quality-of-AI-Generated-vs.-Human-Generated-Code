# Python3 code to demonstrate working of
# Extract K digit Elements Tuples
# Using all() + list comprehension

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# using len() and str() to check length and
# perform string conversion
res = [sub for sub in test_list if all(len(str(ele)) == K for ele in sub)]

# printing result
print("The Extracted tuples : " + str(res))