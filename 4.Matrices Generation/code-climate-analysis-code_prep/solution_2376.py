# Python3 code to demonstrate working of
# Sort String by Custom Substrings
# Using sorted() + zip() + lambda + regex()
import re


# initializing list
test_list = ["Good at 4", "Wake at 7", "Work till 6", "Sleep at 11"]


# printing original list
print("The original list : " + str(test_list))


# initializing substring list
subord_list = ["6", "7", "4", "11"]




# creating inverse mapping with index
temp_dict = {val: key for key, val in enumerate(subord_list)}


# custom sorting
temp_list = sorted([[ele, temp_dict[re.search("(\d+)$", ele).group()]] \
for ele in test_list], key = lambda x: x[1])
# compiling result
res = [ele for ele in list(zip(*temp_list))[0]]

# printing result
print("The sorted list : " + str(res))