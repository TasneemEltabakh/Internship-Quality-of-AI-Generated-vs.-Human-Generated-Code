# Python3 code to demonstrate working of
# All substrings Frequency in String
# Using loop + list comprehension

# initializing string
test_str = "abababa"

# printing original string
print("The original string is : " + str(test_str))

# list comprehension to extract substrings
temp = [test_str[idx: j] for idx in range(len(test_str))
for j in range(idx + 1, len(test_str) + 1)]

# loop to extract final result of frequencies
res = {}
for idx in temp:
if idx not in res.keys():
res[idx] = 1
else:
res[idx] += 1

# printing result
print("Extracted frequency dictionary : " + str(res))