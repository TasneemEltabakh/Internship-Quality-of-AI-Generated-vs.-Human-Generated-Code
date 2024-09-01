# Python3 code to demonstrate working of
# Sort Dictionary by Values Summation
# Using dictionary comprehension + sum() + sorted()

# initializing dictionary
test_dict = {'Gfg' : [6, 7, 4], 'is' : [4, 3, 2], 'best' : [7, 6, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# summing all the values using sum()
temp1 = {val: sum(int(idx) for idx in key)
for val, key in test_dict.items()}

# using sorted to perform sorting as required
temp2 = sorted(temp1.items(), key = lambda ele : temp1[ele[0]])

# rearrange into dictionary
res = {key: val for key, val in temp2}

# printing result
print("The sorted dictionary : " + str(res))