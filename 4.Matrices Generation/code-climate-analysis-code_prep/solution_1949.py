def print_pattern(n):
for i in range(1, n+1, 1):
for j in range(1, n+1, 1):
# check that if index i is
# equal to j
if i == j:


print(j, end=" ")
# if index i is less than j
if i <= j:


for k in range(j+1, n+1, 1):
print(k, end=" ")


for p in range(1, j, 1):
print(p, end=" ")


# print new line
print()




# Driver's code
print_pattern(3)