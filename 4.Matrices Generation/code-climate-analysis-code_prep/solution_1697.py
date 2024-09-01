# Python3 program to find common elements
# in three lists using sets

def IntersecOfSets(arr1, arr2, arr3):
# Converting the arrays into sets
s1 = set(arr1)
s2 = set(arr2)
s3 = set(arr3)

# Calculates intersection of
# sets on s1 and s2
set1 = s1.intersection(s2) #[80, 20, 100]

# Calculates intersection of sets
# on set1 and s3
result_set = set1.intersection(s3)

# Converts resulting set to list
final_list = list(result_set)
print(final_list)

# Driver Code
if __name__ == '__main__' :

# Elements in Array1
arr1 = [1, 5, 10, 20, 40, 80, 100]

# Elements in Array2
arr2 = [6, 7, 20, 80, 100]

# Elements in Array3
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Calling Function
IntersecOfSets(arr1, arr2, arr3)