# Python3 code to demonstrate working of
# Word Index for K position in Strings List
# Using enumerate() + list comprehension

# initializing list
test_list = ["geekforgeeks", "is", "best", "for", "geeks"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 20

# enumerate to get indices of all inner and outer list
res = [ele[0] for sub in enumerate(test_list) for ele in enumerate(sub[1])]

# getting index of word
res = res[K]

# printing result
print("Index of character at Kth position word : " + str(res))