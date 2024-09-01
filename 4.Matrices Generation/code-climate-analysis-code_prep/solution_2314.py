# Python3 code to demonstrate working of
# Maximum occurring Substring from list
# Using regex() + groupby() + max() + lambda
import re
import itertools


# initializing string
test_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
test_list = ['gfg', 'is', 'best']


# printing original string and list
print("The original string is : " + test_str)
print("The original list is : " + str(test_list))


# Maximum occurring Substring from list
# Using regex() + groupby() + max() + lambda
seqs = re.findall(str.join('|', test_list), test_str)
grps = [(key, len(list(j))) for key, j in itertools.groupby(seqs)]
res = max(grps, key = lambda ele : ele[1])

# printing result
print("Maximum frequency substring : " + str(res[0]))