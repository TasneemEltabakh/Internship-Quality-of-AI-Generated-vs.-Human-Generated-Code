def max_min_val(list_val):
     max_val = max(i for i in list_val if isinstance(i, int)) 
     min_val = min(i for i in list_val if isinstance(i, int))
     return(max_val, min_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Original list:")
print(list_val)
print("\nMaximum and Minimum values in the said list:")
print(max_min_val(list_val))
