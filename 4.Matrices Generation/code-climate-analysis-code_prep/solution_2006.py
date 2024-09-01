# Python3 code to demonstrate working of
# Add Space between Potential Words
# Using loop + join()


# initializing list
test_list = ["gfgBest", "forGeeks", "andComputerScience"]


# printing original list
print("The original list : " + str(test_list))


res = []


# loop to iterate all strings
for ele in test_list:
temp = [[]]
for char in ele:

# checking for upper case character
if char.isupper():
temp.append([])

# appending character at latest list
temp[-1].append(char)

# joining lists after adding space
res.append(' '.join(''.join(ele) for ele in temp))


# printing result
print("The space added list of strings : " + str(res))