# Python3 code to demonstrate working of
# Remove multiple empty spaces from string List
# Using loop + strip()

# initializing list
test_list = ['gfg', ' ', ' ', 'is', ' ', 'best']

# printing original list
print("The original list is : " + str(test_list))

# Remove multiple empty spaces from string List
# Using loop + strip()
res = []
for ele in test_list:
if ele.strip():
res.append(ele)

# printing result
print("List after filtering non-empty strings : " + str(res))