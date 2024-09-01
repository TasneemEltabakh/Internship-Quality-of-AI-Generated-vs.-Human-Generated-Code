def matrix_dimensions(test_list):
    row = len(test_list)
    column = len(test_list[0])
    return row,column

lst = [[1,2],[2,4]]
print("\nOriginal list:")
print(lst)
print("Dimension of the said matrix:")
print(matrix_dimensions(lst))
lst = [[0,1,2],[2,4,5]]
print("\nOriginal list:")
print(lst)
print("Dimension of the said matrix:")
print(matrix_dimensions(lst))
lst = [[0,1,2],[2,4,5],[2,3,4]]
print("\nOriginal list:")
print(lst)
print("Dimension of the said matrix:")
print(matrix_dimensions(lst)) 
