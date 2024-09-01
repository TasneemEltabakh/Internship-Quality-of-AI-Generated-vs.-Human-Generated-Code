# Python3 code to demonstrate working of
# Convert dictionary to K Keys dictionaries
# Using loop

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'geeks' : 5, 'CS' : 6}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 2

res = []
count = 0
flag = 0
indict = dict()
for key in test_dict:
indict[key] = test_dict[key]
count += 1

# checking for K size and avoiding empty dict using flag
if count % K == 0 and flag:
res.append(indict)

# reinitializing dictionary
indict = dict()
count = 0
flag = 1


# printing result
print("The converted list : " + str(res))