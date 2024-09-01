import sys
# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

#compute the minimum element of the given 2d array
min=sys.maxsize
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]<=min:
            min=matrix[i][j]

# Display the smallest element of the given matrix
print("The Minimum element of the Given 2d array is: ",min)