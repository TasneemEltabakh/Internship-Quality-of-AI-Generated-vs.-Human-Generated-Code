# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

# compute square of the matrix
for i in range(0,row_size):
    for j in range(0,col_size):
        matrix[i][j]=pow(matrix[i][j],2)

# display square of the matrix
print("Square of the Matrix elements are:")
for m in matrix:
    print(m)