import math
# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

# Calculate sum of the diagonals element
# and Calculate sum of all the element
trace=0
sum=0
for i in range(0, row_size):
    for j in range(0, col_size):
        if i==j:
            trace += matrix[i][j]
        sum+=matrix[i][j]
normal=math.sqrt(sum)

# Display the normal and trace of the matrix
print("Normal Of the Matrix is: ",normal)
print("Trace Of the Matrix is: ",trace)