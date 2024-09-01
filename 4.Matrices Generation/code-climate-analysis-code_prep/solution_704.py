def count_integer(list1):
    ctr = 0
    for i in list1:
        if isinstance(i, int):
            ctr = ctr + 1
    return ctr

list1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

print("Original list:")
print(list1)

print("\nNumber of integers in the said mixed list:")
print(count_integer(list1))
