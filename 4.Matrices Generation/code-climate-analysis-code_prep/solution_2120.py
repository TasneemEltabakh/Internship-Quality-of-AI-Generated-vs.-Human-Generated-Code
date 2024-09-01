# Python program to sort a
# list of tuples alphabetically


# Function to sort the list of
# tuples

def SortTuple(tup):

# Getting the length of list
# of tuples
n = len(tup)

for i in range(n):
for j in range(n-i-1):

if tup[j][0] > tup[j + 1][0]:
tup[j], tup[j + 1] = tup[j + 1], tup[j]

return tup

# Driver's code

tup = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29),
("Nikhil", 21), ("B", "C")]

print(SortTuple(tup))