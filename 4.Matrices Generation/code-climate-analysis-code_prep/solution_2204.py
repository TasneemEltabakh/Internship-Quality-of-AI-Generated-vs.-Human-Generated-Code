# Python3 code to demonstrate working of
# Convert Nested dictionary to Mapped Tuple
# Using list comprehension + generator expression

# initializing dictionary
test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' : {'x' : 1, 'y' : 4},
'best' : {'x' : 8, 'y' : 3}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Nested dictionary to Mapped Tuple
# Using list comprehension + generator expression
res = [(key, tuple(sub[key] for sub in test_dict.values()))
for key in test_dict['gfg']]

# printing result
print("The grouped dictionary : " + str(res))