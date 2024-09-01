size = int(input("Input the size of the matrix: "))
matrix = [[0] * size for row in range(0, size)]
for x in range(0, size):

    line = list(map(int, input().split()))

    for y in range(0, size):
        matrix[x][y] = line[y]

matrix_sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
print("Sum of matrix primary diagonal:")
print(matrix_sum_diagonal)
