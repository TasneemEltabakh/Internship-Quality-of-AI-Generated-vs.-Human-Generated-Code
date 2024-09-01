def sort_sublists(input_list):
    result = list(map(sorted, input_list)) 
    return result
color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
print("\nOriginal list:")
print(color1)  
print("\nAfter sorting each sublist of the said list of lists:")
print(sort_sublists(color1))
