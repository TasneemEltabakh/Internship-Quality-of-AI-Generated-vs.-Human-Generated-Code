# Python3 code to demonstrate
# Test if List contains elements in Range
# using loop

# Initializing loop
test_list = [4, 5, 6, 7, 3, 9]

# printing original list
print("The original list is : " + str(test_list))

# Initialization of range
i, j = 3, 10

# Test if List contains elements in Range
# using loop
res = True
for ele in test_list:
if ele < i or ele >= j :
res = False
break

# printing result
print ("Does list contain all elements in range : " + str(res))