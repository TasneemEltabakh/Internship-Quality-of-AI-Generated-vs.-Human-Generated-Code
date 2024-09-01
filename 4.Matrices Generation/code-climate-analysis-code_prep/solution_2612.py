# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

#Display Lower triangular matrix
print("Lower Triangular Matrix is:\n")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i<j:
            print("0 ",end="")
        else:
            print(matrix[i][j],end=" ")
    print()