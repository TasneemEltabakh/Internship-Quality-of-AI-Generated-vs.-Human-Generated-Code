# Python3 code to demonstrate working of
# Multiple indices Replace in String
# Using loop + join()

# initializing string
test_str = 'geeksforgeeks is best'

# printing original string
print("The original string is : " + test_str)

# initializing list
test_list = [2, 4, 7, 10]

# initializing repl char
repl_char = '*'

# Multiple indices Replace in String
# Using loop + join()
temp = list(test_str)
for idx in test_list:
temp[idx] = repl_char
res = ''.join(temp)

# printing result
print("The String after performing replace : " + str(res))