def heterogeneous_list_to_str(lst):
    result = ','.join(str(x) for x in lst)
    return result
h_data = ["Red", 100, -50, "green", "w,3,r", 12.12, False]
print("Original list:")
print(h_data)
print("\nConvert the heterogeneous list of scalars into a string:")
print(heterogeneous_list_to_str(h_data))
