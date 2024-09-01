# Python3 code to demonstrate working of
# Test if Substring occurs in specific position
# Using loop

# initializing string
test_str = "Gfg is best"

# printing original string
print("The original string is : " + test_str)

# initializing range
i, j = 7, 11

# initializing substr
substr = "best"

# Test if Substring occurs in specific position
# Using loop
res = True
k = 0
for idx in range(len(test_str)):
if idx >= i and idx < j:
if test_str[idx] != substr[k]:
res = False
break
k = k + 1

# printing result
print("Does string contain substring at required position ? : " + str(res))