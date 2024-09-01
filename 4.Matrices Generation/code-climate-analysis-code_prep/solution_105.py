import itertools as it
def permutations_data(iter, length):
    return it.permutations(iter, length)
#List
result = permutations_data(['A','B','C','D'], 3)
print("\nIterator to get specified number of permutations of elements:")
for i in result:
    print(i)

#String
result = permutations_data("Python", 2)
print("\nIterator to get specified number of permutations of elements:")
for i in result:
    print(i)
