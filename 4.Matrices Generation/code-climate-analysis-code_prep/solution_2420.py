# Python3 code to demonstrate
# Reverse Row sort in Lists of List
# using loop

# initializing list
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

# printing original list
print ("The original list is : " + str(test_list))

# Reverse Row sort in Lists of List
# using loop
for ele in test_list:
ele.sort(reverse = True)

# printing result
print ("The reverse sorted Matrix is : " + str(test_list))