import sys
# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

#compute the maximum element of the given 2d array
max=-sys.maxsize-1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]>=max:
            max=matrix[i][j]

# Display the largest element of the given matrix
print("The Maximum element of the Given 2d array is: ",max)