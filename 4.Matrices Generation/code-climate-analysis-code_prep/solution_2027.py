# Python3 code to demonstrate
# Split String of list on K character
# using loop + split()

# Initializing list
test_list = ['Gfg is best', 'for Geeks', 'Preparing']

# printing original list
print("The original list is : " + str(test_list))

K = ' '

# Split String of list on K character
# using loop + split()
res = []
for ele in test_list:
sub = ele.split(K)
res.extend(sub)

# printing result
print ("The extended list after split strings : " + str(res))