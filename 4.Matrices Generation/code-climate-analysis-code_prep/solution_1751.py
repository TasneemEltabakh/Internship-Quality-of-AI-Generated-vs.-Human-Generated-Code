# Python3 code to demonstrate
# Prefix frequency in List
# using loop + startswith()

# Initializing list
test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

# printing original list
print("The original list is : " + str(test_list))

# Initializing substring
test_sub = 'gfg'

# Prefix frequency in List
# using loop + startswith()
res = 0
for ele in test_list:
if ele.startswith(test_sub):
res = res + 1

# printing result
print ("Strings count with matching frequency : " + str(res))