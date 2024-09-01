# Python 3 code to demonstrate
# Duplication Removal List Product
# using naive methods


# getting Product
def prod(val) :
res = 1
for ele in val:
res *= ele
return res


# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))


# using naive method
# Duplication Removal List Product
res = []
for i in test_list:
if i not in res:
res.append(i)
res = prod(res)


# printing list after removal
print ("Duplication removal list product : " + str(res))