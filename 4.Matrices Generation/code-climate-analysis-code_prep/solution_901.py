def test(dictt,keys):
    return [list(d[k] for k in keys) for d in dictt] 

students = [
        {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
        {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
        {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
        {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
        {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
        ]

print("\nOriginal Dictionary:")
print(students)
print("\nExtract values from the said dictionarie and create a list of lists using those values:")
print("\n",test(students,('student_id', 'name', 'class')))
print("\n",test(students,('student_id', 'name')))
print("\n",test(students,('name', 'class')))
