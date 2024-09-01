def tuple_int_str(tuple_str):
    result = tuple(map(lambda x: (int(x[0]), int(x[2])), tuple_str))
    return result     
tuple_str =  (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
print("Original tuple values:")
print(tuple_str)
print("\nNew tuple values:")
print(tuple_int_str(tuple_str))
