# Python3 code to demonstrate working of
# Split Strings on Prefix Occurrence
# Using loop + startswith()


# initializing list
test_list = ["geeksforgeeks", "best", "geeks", "and", "geeks", "love", "CS"]


# printing original list
print("The original list is : " + str(test_list))


# initializing prefix
pref = "geek"




res = []
for val in test_list:

# checking for prefix
if val.startswith(pref):

# if pref found, start new list
res.append([val])
else:

# else append in current list
res[-1].append(val)


# printing result
print("Prefix Split List : " + str(res))