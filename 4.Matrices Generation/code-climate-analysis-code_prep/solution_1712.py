# Python3 code to demonstrate
# Pair elements with Rear element in Matrix Row
# using list comprehension

# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]

# printing original list
print("The original list is : " + str(test_list))

# Pair elements with Rear element in Matrix Row
# using list comprehension
res = []
for sub in test_list:
res.append([[ele, sub[-1]] for ele in sub[:-1]])

# printing result
print ("The list after pairing is : " + str(res))