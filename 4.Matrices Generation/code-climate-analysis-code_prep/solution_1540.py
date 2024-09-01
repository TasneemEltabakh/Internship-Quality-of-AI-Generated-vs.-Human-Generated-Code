def decimal_to_binary_list(n):
    result = [int(x) for x in list('{0:0b}'.format(n))]
    return result
n = 8
print("Original Number:",n)
print("Decimal number (",n,") to binary list:")
print(decimal_to_binary_list(n))
n = 45
print("\nOriginal Number:",n)
print("Decimal number (",n,") to binary list:")
print(decimal_to_binary_list(n))
n = 100
print("\nOriginal Number:",n)
print("Decimal number (",n,") to binary list:")
print(decimal_to_binary_list(n))
