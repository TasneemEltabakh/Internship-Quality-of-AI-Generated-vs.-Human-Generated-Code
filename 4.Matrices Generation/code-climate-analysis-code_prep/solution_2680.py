# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

# Compute transpose of two matrices
tran_matrix=[[0 for i in range(col_size)] for i in range(row_size)]
for i in range(0,row_size):
    for j in range(0,col_size):
        tran_matrix[i][j]=matrix[j][i]

# display transpose of the matrix
print("Transpose of the Given Matrix is:")
for m in tran_matrix:
    print(m)