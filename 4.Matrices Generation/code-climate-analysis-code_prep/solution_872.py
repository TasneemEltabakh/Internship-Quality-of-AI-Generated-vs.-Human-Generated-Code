def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Original list:")
print(list_val)
print("\nMaximum values in the said list using lambda:")
print(max_val(list_val))
