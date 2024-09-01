# Get size of matrix
row_size=int(input("Enter the row Size Of the Matrix:"))
col_size=int(input("Enter the columns Size Of the Matrix:"))

matrix=[]
# Taking input of the 1st matrix
print("Enter the Matrix Element:")
for i in range(row_size):
    matrix.append([int(j) for j in input().split()])

count_zero=0
#Count number of zeros present in the given Matrix
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            count_zero+=1

#check if zeros present in the given Matrix>(row*column)/2
if count_zero>(row_size*col_size)//2:
    print("Given Matrix is a sparse Matrix.")
else:
    print("Given Matrix is not a sparse Matrix.")