# Python3 code to demonstrate working of
# Convert Character Matrix to single String
# Using join() + list comprehension

# initializing list
test_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]

# printing original list
print("The original list is : " + str(test_list))

# Convert Character Matrix to single String
# Using join() + list comprehension
res = ''.join(ele for sub in test_list for ele in sub)

# printing result
print("The String after join : " + res)