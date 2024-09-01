# Python3 code to demonstrate working of
# Maximum Consecutive Substring Occurrence
# Using max() + re.findall()
import re

# initializing string
test_str = 'geeksgeeks are geeks for all geeksgeeksgeeks'

# printing original string
print("The original string is : " + str(test_str))

# initializing subs
sub_str = 'geeks'

# Maximum Consecutive Substring Occurrence
# Using max() + re.findall()
res = max(re.findall('((?:' + re.escape(sub_str) + ')*)', test_str), key = len)

# printing result
print("The maximum run of Substring : " + res)