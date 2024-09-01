# Python3 code to demonstrate working of
# Convert Integer Matrix to String Matrix
# Using str() + list comprehension

# initializing list
test_list = [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]

# printing original list
print("The original list : " + str(test_list))

# using str() to convert each element to string
res = [[str(ele) for ele in sub] for sub in test_list]

# printing result
print("The data type converted Matrix : " + str(res))