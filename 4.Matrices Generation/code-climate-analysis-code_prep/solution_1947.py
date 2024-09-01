# Python3 code to demonstrate working of
# Dictionary Values Mean
# Using loop + len()

# initializing dictionary
test_dict = {"Gfg" : 4, "is" : 7, "Best" : 8, "for" : 6, "Geeks" : 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# loop to sum all values
res = 0
for val in test_dict.values():
res += val

# using len() to get total keys for mean computation
res = res / len(test_dict)

# printing result
print("The computed mean : " + str(res))