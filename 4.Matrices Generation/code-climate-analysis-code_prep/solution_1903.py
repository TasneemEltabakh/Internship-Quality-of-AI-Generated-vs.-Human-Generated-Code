# Python3 code to demonstrate working of
# Sort Tuples by Total digits
# Using sort() + len() + sum()

def count_digs(tup):

# gets total digits in tuples
return sum([len(str(ele)) for ele in tup ])

# initializing list
test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
test_list.sort(key = count_digs)

# printing result
print("Sorted tuples : " + str(test_list))