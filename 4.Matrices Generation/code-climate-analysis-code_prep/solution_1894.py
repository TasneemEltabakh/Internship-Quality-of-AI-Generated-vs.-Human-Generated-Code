# Python3 code to demonstrate working of
# Unique elements in nested tuple
# Using nested loop + set()

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list
print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using nested loop + set()
res = []
temp = set()
for inner in test_list:
for ele in inner:
if not ele in temp:
temp.add(ele)
res.append(ele)

# printing result
print("Unique elements in nested tuples are : " + str(res))