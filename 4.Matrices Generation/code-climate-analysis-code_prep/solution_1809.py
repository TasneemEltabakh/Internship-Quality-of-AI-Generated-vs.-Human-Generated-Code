# Python Program to Print
# all subsets of given size of a set


import itertools


def findsubsets(s, n):
return list(itertools.combinations(s, n))


# Driver Code
s = {1, 2, 3}
n = 2


print(findsubsets(s, n))