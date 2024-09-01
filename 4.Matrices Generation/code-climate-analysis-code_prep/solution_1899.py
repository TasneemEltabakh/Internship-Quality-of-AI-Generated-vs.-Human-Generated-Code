# function to display the pattern up to n
def display(n):

print("*")

for i in range(1, n+1):
print("*", end="")

# for loop to display number up to i
for j in range(1, i+1):
print(j, end="")

# for loop to display number in reverse direction
for j in range(i-1, 0, -1):
print(j, end="")

print("*", end="")
print()

# for loop to display i in reverse direction
for i in range(n-1, 0, -1):
print("*", end="")
for j in range(1, i+1):
print(j, end="")

for j in range(i-1, 0, -1):
print(j, end="")

print("*", end="")
print()

print("*")


# driver code
n = 5
print('\nFor n =', n)
display(n)

n = 3
print('\nFor n =', n)
display(n)