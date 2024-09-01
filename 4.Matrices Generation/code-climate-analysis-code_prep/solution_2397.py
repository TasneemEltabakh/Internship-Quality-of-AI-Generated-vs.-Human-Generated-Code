# define a function for finding
# the maximum for adjacent
# pairs in the array
def maximumAdjacent(arr1, n):

# array to store the max
# value between adjacent pairs
arr2 = []

# iterate from 1 to n - 1
for i in range(1, n):

# find max value between
# adjacent pairs gets
# stored in r
r = max(arr1[i], arr1[i-1])

# add element
arr2.append(r)

# printing the elements
for ele in arr2 :
print(ele,end=" ")

if __name__ == "__main__" :

# size of the input array
n = 6

# input array
arr1 = [1,2,2,3,4,5]

# function calling
maximumAdjacent(arr1, n)