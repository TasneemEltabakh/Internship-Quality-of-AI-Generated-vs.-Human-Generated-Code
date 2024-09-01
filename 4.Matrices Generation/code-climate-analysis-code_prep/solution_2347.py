# importing libraries
import sys
import math as mt
t = 1
# store prime to reduce overflow
mod = 9007199254740881


for ___ in range(t):


# string to check number of distinct substring
s = 'abcd'


# to store substrings
l = []


# to store hash values by Rabin Karp algorithm
d = {}


for i in range(len(s)):
suma = 0
pre = 0


# Number of input alphabets
D = 256


for j in range(i, len(s)):


# calculate new hash value by adding next element
pre = (pre*D+ord(s[j])) % mod


# store string length if non repeat
if d.get(pre, -1) == -1:
l.append([i, j])
d[pre] = 1


# resulting length
print(len(l))


# resulting distinct substrings
for i in range(len(l)):
print(s[l[i][0]:l[i][1]+1], end=" ")