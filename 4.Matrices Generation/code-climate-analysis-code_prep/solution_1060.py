def checkSubset(input_list1, input_list2): 
    return all(map(input_list1.__contains__, input_list2)) 
      

list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]] 
list2 = [[1, 3],[13,15,17]]   
print("Original list:")
print(list1)
print(list2)
print("\nIf the one of the said list is a subset of another.:")
print(checkSubset(list1, list2)) 

list1 = [
           [
             [1,2],[2,3]
           ],
           [
             [3,4],[5,6]
           ]
         ]
list2 = [
           [
             [3,4], [5, 6]
           ]
         ]
print("Original list:")
print(list1)
print(list2)
print("\nIf the one of the said list is a subset of another.:")
print(checkSubset(list1, list2)) 
list1 = [
           [
             [1,2],[2,3]
           ],
           [
             [3,4],[5,7]
           ]
         ]
list2 = [
           [
             [3,4], [5, 6]
           ]
         ]
print("Original list:")
print(list1)
print(list2)
print("\nIf the one of the said list is a subset of another.:")
print(checkSubset(list1, list2))
