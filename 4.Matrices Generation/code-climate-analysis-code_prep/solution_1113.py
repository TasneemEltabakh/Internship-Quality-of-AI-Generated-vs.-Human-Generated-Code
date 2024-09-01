def sort_sublists(input_list):
    input_list.sort()  # sort by sublist contents
    input_list.sort(key=len)
    return input_list

list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nSort the list of lists by length and value:")
print(sort_sublists(list1))
