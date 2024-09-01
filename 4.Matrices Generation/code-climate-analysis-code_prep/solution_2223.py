# Python3 code to demonstrate working of
# Right and Left Shift characters in String
# Using String multiplication + string slicing

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + test_str)

# initializing right rot
r_rot = 7

# initializing left rot
l_rot = 3

# Right and Left Shift characters in String
# Using String multiplication + string slicing
res = (test_str * 3)[len(test_str) + r_rot - l_rot :
2 * len(test_str) + r_rot - l_rot]

# printing result
print("The string after rotation is : " + str(res))