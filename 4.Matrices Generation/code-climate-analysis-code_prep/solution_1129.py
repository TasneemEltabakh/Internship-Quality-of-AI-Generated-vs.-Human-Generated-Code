def test(lst):
    result = {item[0]: item[1:] for item in lst}
    return result

students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]

print("\nOriginal list of lists:")
print(students)
print("\nConvert the said list of lists to a dictionary:")
print(test(students))
