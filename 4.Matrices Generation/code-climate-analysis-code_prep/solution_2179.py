# Python3 code to demonstrate working of
# Matrix Row subset
# Using any() + all() + list comprehension

# initializing lists
test_list = [[4, 5, 7], [2, 3, 4], [9, 8, 0]]

# printing original list
print("The original list is : " + str(test_list))

# initializing check Matrix
check_matr = [[2, 3], [1, 2], [9, 0]]

# Matrix Row subset
# Using any() + all() + list comprehension
res = [ele for ele in check_matr if any(all(a in sub for a in ele)
for sub in test_list)]

# printing result
print("Matrix row subsets : " + str(res))