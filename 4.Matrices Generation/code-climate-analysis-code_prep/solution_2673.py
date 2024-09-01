# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

#Calculate sum of lower triangular matrix element
sum=0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i<j:
            sum += matrix[i][j]

# display the sum of a lower triangular matrix element
print("Sum of Lower Triangular Matrix Elements is: ",sum)