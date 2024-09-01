# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the 1st matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

sum=0
#Calculate sum of the diagonals element
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i==j:
            sum+=matrix[i][j]
# Display the sum of diagonals Element
print("Sum of diagonals Element is: ",sum)