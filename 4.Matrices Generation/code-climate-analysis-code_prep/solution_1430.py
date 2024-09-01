def test(list1, list2):
    result =  set(list1).intersection(list2)
    return list(result)
list1 =  [('red', 'green'), ('black', 'white'), ('orange', 'pink')] 
list2 =  [('red', 'green'), ('orange', 'pink')] 
print("\nOriginal lists:")
print(list1)
print(list2)
print("\nCommon tuples between two said lists")
print(test(list1,list2)) 
list1 =  [('red', 'green'), ('orange', 'pink')] 
list2 =  [('red', 'green'), ('black', 'white'), ('orange', 'pink')] 
print("\nOriginal lists:")
print(list1)
print(list2)
print("\nCommon tuples between two said lists")
print(test(list1,list2))
