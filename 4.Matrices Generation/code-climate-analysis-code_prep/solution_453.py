import itertools
def combination(str1):
    result = map(''.join, itertools.product(*((c.lower(), c.upper()) for c in str1)))
    return list(result)
st ="abc"
print("Original string:")
print(st)
print("All lower and upper mixed case combinations of the said string:")
print(combination(st))
st ="w3r"
print("\nOriginal string:")
print(st)
print("All lower and upper mixed case combinations of the said string:")
print(combination(st))
st ="Python"
print("\nOriginal string:")
print(st)
print("All lower and upper mixed case combinations of the said string:")
print(combination(st))
