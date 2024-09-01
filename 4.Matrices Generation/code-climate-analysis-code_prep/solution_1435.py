import itertools as it
def combinations_data(iter, length):
    return it.combinations(iter, length)
#List
result = combinations_data(['A','B','C','D'], 1)
print("\nCombinations of an given iterable of length 1:")
for i in result:
    print(i)

#String
result = combinations_data("Python", 1)
print("\nCombinations of an given iterable of length 1:")
for i in result:
    print(i)
    
#List
result = combinations_data(['A','B','C','D'], 2)
print("\nCombinations of an given iterable of length 2:")
for i in result:
    print(i)

#String
result = combinations_data("Python", 2)
print("\nCombinations of an given iterable of length 2:")
for i in result:
    print(i)
