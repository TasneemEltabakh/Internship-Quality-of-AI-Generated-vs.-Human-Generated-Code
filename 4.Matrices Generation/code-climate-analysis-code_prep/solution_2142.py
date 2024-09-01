# Python3 code to demonstrate
# Replace Substrings from String List
# using loop + replace() + enumerate()

# Initializing list1
test_list1 = ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
test_list2 = [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Replace Substrings from String List
# using loop + replace() + enumerate()
sub = dict(test_list2)
for key, val in sub.items():
for idx, ele in enumerate(test_list1):
if key in ele:
test_list1[idx] = ele.replace(key, val)

# printing result
print ("The list after replacement : " + str(test_list1))