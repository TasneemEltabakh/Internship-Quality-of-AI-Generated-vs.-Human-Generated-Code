# Python3 code to demonstrate working of
# Remove keys with Values Greater than K ( Including mixed values )
# Using loop + isinstance()

# initializing dictionary
test_dict = {'Gfg' : 3, 'is' : 7, 'best' : 10, 'for' : 6, 'geeks' : 'CS'}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 6

# using loop to iterate keys of dictionary
res = {}
for key in test_dict:

# testing for data type and then condition, order is imp.
if not (isinstance(test_dict[key], int) and test_dict[key] > K):
res[key] = test_dict[key]

# printing result
print("The constructed dictionary : " + str(res))