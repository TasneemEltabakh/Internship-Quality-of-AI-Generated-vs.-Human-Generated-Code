def count_list(input_list): 
    return len(input_list) 
      
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]] 
list2 = [[2, 4], [[6,8], [4,5,8]], [10, 12, 14]]   
print("Original list:")
print(list1)
print("\nNumber of lists in said list of lists:")
print(count_list(list1))
print("\nOriginal list:")
print(list2)
print("\nNumber of lists in said list of lists:")
print(count_list(list2))
