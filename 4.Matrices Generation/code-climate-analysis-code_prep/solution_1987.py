# Python3 code to demonstrate working of
# Split by repeating substring
# Using * operator + len()

# initializing string
test_str = "gfggfggfggfggfggfggfggfg"

# printing original string
print("The original string is : " + test_str)

# initializing target
K = 'gfg'

# Split by repeating substring
# Using * operator + len()
temp = len(test_str) // len(str(K))
res = [K] * temp

# printing result
print("The split string is : " + str(res))