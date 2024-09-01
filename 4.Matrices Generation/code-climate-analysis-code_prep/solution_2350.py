# Python3 code to demonstrate working of
# Convert List of Dictionaries to List of Lists
# Using loop + enumerate()

# initializing list
test_list = [{'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
{'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
{'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}]

# printing original list
print("The original list is : " + str(test_list))

# Convert List of Dictionaries to List of Lists
# Using loop + enumerate()
res = []
for idx, sub in enumerate(test_list, start = 0):
if idx == 0:
res.append(list(sub.keys()))
res.append(list(sub.values()))
else:
res.append(list(sub.values()))

# printing result
print("The converted list : " + str(res))