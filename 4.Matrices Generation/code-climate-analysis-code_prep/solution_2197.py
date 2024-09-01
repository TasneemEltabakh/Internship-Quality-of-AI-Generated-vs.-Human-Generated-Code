# Python3 code to demonstrate working of
# Remove Dictionary Key Words
# Using split() + loop + replace()

# initializing string
test_str = 'gfg is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing Dictionary
test_dict = {'geeks' : 1, 'best': 6}

# Remove Dictionary Key Words
# Using split() + loop + replace()
for key in test_dict:
if key in test_str.split(' '):
test_str = test_str.replace(key, "")

# printing result
print("The string after replace : " + str(test_str))