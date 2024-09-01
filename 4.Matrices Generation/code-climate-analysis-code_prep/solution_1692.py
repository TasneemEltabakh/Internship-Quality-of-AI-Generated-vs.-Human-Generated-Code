# Python3 code to demonstrate working of
# Avoid Last occurrence of delimitter
# Using map() + join() + str()

# initializing list
test_list = [4, 7, 8, 3, 2, 1, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing delim
delim = "$"

# appending delim to join
# will leave stray "$" at end
res = ''
for ele in test_list:
res += str(ele) + "$"

# removing last using slicing
res = res[:len(res) - 1]

# printing result
print("The joined string : " + str(res))