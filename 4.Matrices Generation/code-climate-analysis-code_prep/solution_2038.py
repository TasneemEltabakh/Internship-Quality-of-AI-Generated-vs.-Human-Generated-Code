# Python3 code to demonstrate
# Reverse All Strings in String List
# using list comprehension

# initializing list
test_list = ["geeks", "for", "geeks", "is", "best"]

# printing original list
print ("The original list is : " + str(test_list))

# using list comprehension
# Reverse All Strings in String List
res = [i[::-1] for i in test_list]

# printing result
print ("The reversed string list is : " + str(res))