# Python code to demonstrate
# Count Strings with substring String List
# using list comprehension + len()

# initializing list
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# printing original list
print ("The original list is : " + str(test_list))

# initializing substring
subs = 'Geek'

# using list comprehension + len()
# Count Strings with substring String List
res = len([i for i in test_list if subs in i])

# printing result
print ("All strings count with given substring are : " + str(res))