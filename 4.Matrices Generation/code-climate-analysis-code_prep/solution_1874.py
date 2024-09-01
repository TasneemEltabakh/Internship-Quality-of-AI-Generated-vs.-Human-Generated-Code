# Python3 code to demonstrate working of
# Remove after substring in String
# Using index() + len() + slicing

# initializing strings
test_str = 'geeksforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing sub string
sub_str = "best"

# slicing off after length computation
res = test_str[:test_str.index(sub_str) + len(sub_str)]

# printing result
print("The string after removal : " + str(res))