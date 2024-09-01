# Python3 code to demonstrate working of
# Convert Lists of List to Dictionary
# Using loop

# initializing list
test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

# printing original list
print("The original list is : " + str(test_list))

# Convert Lists of List to Dictionary
# Using loop
res = dict()
for sub in test_list:
res[tuple(sub[:2])] = tuple(sub[2:])

# printing result
print("The mapped Dictionary : " + str(res))