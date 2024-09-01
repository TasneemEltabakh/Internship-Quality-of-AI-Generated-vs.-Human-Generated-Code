# Python3 code to demonstrate working of
# Replace String by Kth Dictionary value
# Using list comprehension

# initializing list
test_list = ["Gfg", "is", "Best"]

# printing original list
print("The original list : " + str(test_list))

# initializing subs. Dictionary
subs_dict = {
"Gfg" : [5, 6, 7],
"is" : [7, 4, 2],
}

# initializing K
K = 2

# using list comprehension to solve
# problem using one liner
res = [ele if ele not in subs_dict else subs_dict[ele][K]
for ele in test_list]

# printing result
print("The list after substitution : " + str(res))