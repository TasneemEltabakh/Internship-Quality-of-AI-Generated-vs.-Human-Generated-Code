# Get size of 1st matrix
row_size=int(input("Enter the row Size Of the 1st Matrix:"))
col_size=int(input("Enter the columns Size Of the 1st Matrix:"))

# Get size of 2nd matrix
row_size1=int(input("Enter the row Size Of the 1st Matrix:"))
col_size1=int(input("Enter the columns Size Of the 2nd Matrix:"))

matrix=[]
# Taking input of the 1st matrix
print("Enter the 1st Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

matrix1=[]
# Taking input of the 2nd matrix
print("Enter the 2nd Matrix Element:")
for i in range(row_size):
    matrix1.append([int(j) for j in input().split()])

# Compare two matrices
point=0
if row_size==row_size1 and col_size==col_size1:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix1[i][j]:
                point=1
                break
else:
    print("Two matrices are not equal.")
    exit(0)

if point==1:
    print("Two matrices are not equal.")
else:
    print("Two matrices are equal.")