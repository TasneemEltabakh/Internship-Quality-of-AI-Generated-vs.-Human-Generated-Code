# Python program to find the sum
# and average of the list

L = [4, 5, 1, 2, 9, 7, 10, 8]


# variable to store the sum of
# the list
count = 0

# Finding the sum
for i in L:
count += i

# divide the total elements by
# number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)