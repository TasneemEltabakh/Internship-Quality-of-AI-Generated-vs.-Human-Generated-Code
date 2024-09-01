from operator import itemgetter

def max_min_list_tuples(class_students):
    return_max = max(class_students,key=itemgetter(1))[1] 
    return_min = min(class_students,key=itemgetter(1))[1] 
    return return_max, return_min
   
class_students = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
print("Original list with tuples:")
print(class_students)
print("\nMaximum and minimum values of the said list of tuples:")
print(max_min_list_tuples(class_students))
