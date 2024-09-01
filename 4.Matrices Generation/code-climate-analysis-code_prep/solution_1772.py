# Python3 code to demonstrate working of
# Replace words from Dictionary
# Using split() + join() + get()

# initializing string
test_str = 'geekforgeeks best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# lookup Dictionary
lookp_dict = {"best" : "good and better", "geeks" : "all CS aspirants"}

# performing split()
temp = test_str.split()
res = []
for wrd in temp:

# searching from lookp_dict
res.append(lookp_dict.get(wrd, wrd))

res = ' '.join(res)

# printing result
print("Replaced Strings : " + str(res))