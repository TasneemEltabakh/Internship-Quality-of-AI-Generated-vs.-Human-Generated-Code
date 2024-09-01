import itertools
def permutations_all(l):
    for values in itertools.permutations(l):
        print(values)

permutations_all([1])
print("\n")
permutations_all([1,2])
print("\n")
permutations_all([1,2,3])
