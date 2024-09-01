# Python3 code to demonstrate working of
# Sort Matrix by index-value equality count
# Using sort() + len() + enumerate()


def get_idx_ele_count(row):

# getting required count
# element and index compared, if equal added
# in list, length computed using len()
return len([ele for idx, ele in enumerate(row) if ele == idx])


# initializing list
test_list = [[3, 1, 2, 5, 4], [0, 1, 2, 3, 4],
[6, 5, 4, 3, 2], [0, 5, 4, 2]]

# printing original list
print("The original list is : " + str(test_list))

# inplace sorting using sort()
test_list.sort(key=get_idx_ele_count)

# printing result
print("Sorted List : " + str(test_list))