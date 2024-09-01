rows = int(input("Input rows: "))
columns = int(input("Input columns: "))
matrix = [[0]*columns for row in range(rows)]
print('Input number of elements in a row (1, 2, 3): ')
for row in range(rows):
    lines = list(map(int, input().split()))
    for column in range(columns):
        matrix[row][column] = lines[column]

sum = [0]*columns
print("sum for each column:")
for column in range(columns):
    for row in range(rows):
        sum[column] += matrix[row][column]
    print((sum[column]), ' ', end = '')
