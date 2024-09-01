# Python3 code to demonstrate working of
# Extract elements filtered by substring
# from other list Using zip() + loop + in
# operator

# initializing list
test_list1 = ["Gfg", "is", "not", "best", "and",
"not", "for", "CS"]
test_list2 = ["Its ok", "all ok", "wrong", "looks ok",
"ok", "wrong", "ok", "thats ok"]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing substr
sub_str = "ok"

res = []
# using zip() to map by index
for ele1, ele2 in zip(test_list1, test_list2):

# checking for substring
if sub_str in ele2:
res.append(ele1)

# printing result
print("The extracted list : " + str(res))