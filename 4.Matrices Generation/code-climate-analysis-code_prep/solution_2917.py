# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the 1st matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

matrix1=[]
# Taking input of the 2nd matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix1.append([int(j) for j in input().split()])

# Compute Subtraction of two matrices
sub_matrix=[[0 for i in range(col_size)] for i in range(row_size)]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        sub_matrix[i][j]=matrix[i][j]-matrix1[i][j]

# display the Subtraction of two matrices
print("Subtraction of the two Matrices is:")
for m in sub_matrix:
    print(m)