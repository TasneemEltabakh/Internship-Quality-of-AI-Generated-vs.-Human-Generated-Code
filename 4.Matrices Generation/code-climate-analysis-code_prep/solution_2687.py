# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

# Calculate sum of given matrix Elements
sum=0
for i in range(0,row_size):
    for j in range(0,col_size):
        sum+=matrix[i][j]

# Display The Sum Of Given Matrix Elements
print("Sum of the Given Matrix Elements is: ",sum)