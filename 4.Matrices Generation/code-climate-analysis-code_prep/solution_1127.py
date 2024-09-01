def test(lst):
    return [lst for lst in lst if isinstance(lst, int)]
mixed_list = [34.67, 12, -94.89, "Python", 0, "C#"]
print("Original list:", mixed_list)
print("After removing all the values except integer values from the said array of mixed values:")
print(test(mixed_list)) 
