def convert_to_int(lst):
    result = [dict([a, int(x)] for a, x in b.items()) for b in lst]
    return result

def convert_to_float(lst):
    result = [dict([a, float(x)] for a, x in b.items()) for b in lst]
    return result

nums =[{ 'x':'10' , 'y':'20' , 'z':'30' }, { 'p':'40', 'q':'50', 'r':'60'}]
print("Original list:")
print(nums)
print("\nString values of a given dictionary, into integer types:")
print(convert_to_int(nums))
nums =[{ 'x':'10.12', 'y':'20.23', 'z':'30'}, { 'p':'40.00', 'q':'50.19', 'r':'60.99'}]
print("\nOriginal list:")
print(nums)
print("\nString values of a given dictionary, into float types:")
print(convert_to_float(nums))
