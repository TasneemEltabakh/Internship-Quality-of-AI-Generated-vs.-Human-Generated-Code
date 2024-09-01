# Python3 code to demonstrate working of
# Scoring Matrix using Dictionary
# Using loop

# initializing list
test_list = [['gfg', 'is', 'best'], ['gfg', 'is', 'for', 'geeks']]

# printing original list
print("The original list is : " + str(test_list))

# initializing test dict
test_dict = {'gfg' : 5, 'is' : 10, 'best' : 13, 'for' : 2, 'geeks' : 15}

# Scoring Matrix using Dictionary
# Using loop
res = []
for sub in test_list:
sum = 0
for val in sub:
if val in test_dict:
sum += test_dict[val]
res.append(sum)

# printing result
print("The Row scores : " + str(res))