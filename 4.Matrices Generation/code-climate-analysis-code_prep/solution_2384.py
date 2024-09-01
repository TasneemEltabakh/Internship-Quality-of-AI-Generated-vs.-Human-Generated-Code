# Python3 code to demonstrate working of
# Replace Different characters in String at Once
# using join() + generator expression


# initializing string
test_str = 'geeksforgeeks is best'


# printing original String
print("The original string is : " + str(test_str))


# initializing mapping dictionary
map_dict = {'e':'1', 'b':'6', 'i':'4'}


# generator expression to construct vals
# join to get string
res = ''.join(idx if idx not in map_dict else map_dict[idx] for idx in test_str)


# printing result
print("The converted string : " + str(res))