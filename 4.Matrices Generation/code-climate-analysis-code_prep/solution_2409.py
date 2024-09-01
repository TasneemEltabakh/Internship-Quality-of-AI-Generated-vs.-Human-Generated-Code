# Python3 code to demonstrate working of
# Extract words starting with K in String List
# Using loop + split()

# initializing list
test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = "g"

res = []
for sub in test_list:
# splitting phrases
temp = sub.split()
for ele in temp:

# checking for matching elements
if ele[0].lower() == K.lower():
res.append(ele)

# printing result
print("The filtered elements : " + str(res))