

# function that takes arbitary
# number of inputs
def avgfun(*n):
sums = 0

for t in n:
sums = sums + t

avg = sums / len(n)
return avg


# Driver Code
result1 = avgfun(1, 2, 3)
result2 = avgfun(2, 6, 4, 8)

# Printing average of the list
print(round(result1, 2))
print(round(result2, 2))