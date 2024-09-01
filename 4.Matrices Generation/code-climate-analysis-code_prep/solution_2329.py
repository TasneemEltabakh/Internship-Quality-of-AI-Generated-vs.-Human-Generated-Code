# Python3 code to demonstrate
# Group Sublists by another List
# using loop + generator(yield)

# helper function
def grp_ele(test_list1, test_list2):
temp = []
for i in test_list1:
if i in test_list2:
if temp:
yield temp
temp = []
yield i
else:
temp.append(i)
if temp:
yield temp

# Initializing lists
test_list1 = [8, 5, 9, 11, 3, 7]
test_list2 = [9, 11]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Group Sublists by another List
# using loop + generator(yield)
res = list(grp_ele(test_list1, test_list2))

# printing result
print ("The Grouped list is : " + str(res))