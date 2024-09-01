# Python3 code to demonstrate working of
# Filter dictionary values in heterogeneous dictionary
# Using type() + dictionary comprehension

# initializing dictionary
test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 3, 'for' : 'geeks'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing K
K = 3

# Filter dictionary values in heterogeneous dictionary
# Using type() + dictionary comprehension
res = {key : val for key, val in test_dict.items()
if type(val) != int or val > K}

# printing result
print("Values greater than K : " + str(res))