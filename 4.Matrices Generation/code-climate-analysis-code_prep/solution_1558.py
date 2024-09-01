import itertools as it
def tee_data(iter, n):
    return it.tee(iter, n)
#List
result = tee_data(['A','B','C','D'], 5)
print("Generate iterables specified number of times:")
for i in result:
    print(list(i))

#String
result = tee_data("Python itertools", 4)
print("\nGenerate iterables specified number of times:")
for i in result:
    print(list(i))
