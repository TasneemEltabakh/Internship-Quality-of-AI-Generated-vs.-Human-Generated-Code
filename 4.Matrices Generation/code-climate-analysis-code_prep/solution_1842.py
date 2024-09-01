# Python3 code to demonstrate working of
# Exceptional Split in String
# Using loop + split()

# initializing string
test_str = "gfg, is, (best, for), geeks"

# printing original string
print("The original string is : " + test_str)

# Exceptional Split in String
# Using loop + split()
temp = ''
res = []
check = 0
for ele in test_str:
if ele == '(':
check += 1
elif ele == ')':
check -= 1
if ele == ', ' and check == 0:
if temp.strip():
res.append(temp)
temp = ''
else:
temp += ele
if temp.strip():
res.append(temp)

# printing result
print("The string after exceptional split : " + str(res))