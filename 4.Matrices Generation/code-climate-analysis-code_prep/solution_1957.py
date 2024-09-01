# Python3 code to demonstrate working of
# Substring presence in Strings List
# Using loop

# initializing lists
test_list1 = ["Gfg", "is", "Best"]
test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]

# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))

# using loop to iterate
res = []
for ele in test_list1 :
temp = False

# inner loop to check for
# presence of element in any list
for sub in test_list2 :
if ele in sub:
temp = True
break
res.append(temp)

# printing result
print("The match list : " + str(res))