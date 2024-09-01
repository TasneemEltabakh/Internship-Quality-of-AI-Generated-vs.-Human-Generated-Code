# Python3 code to demonstrate
# Remove words containing list characters
# using list comprehension + all()
from itertools import groupby

# initializing list
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# initializing char list
char_list = ['g', 'o']

# printing original list
print ("The original list is : " + str(test_list))

# printing character list
print ("The character list is : " + str(char_list))

# Remove words containing list characters
# using list comprehension + all()
res = [ele for ele in test_list if all(ch not in ele for ch in char_list)]

# printing result
print ("The filtered strings are : " + str(res))