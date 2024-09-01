from itertools import product
def test(dictt):
    result = [dict(zip(dictt, sub)) for sub in product(*dictt.values())]
    return result

students = {1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}

print("\nOriginal dictionary:")
print(students)
print("\nA key-value list pairings of the said dictionary:")
print(test(students))
