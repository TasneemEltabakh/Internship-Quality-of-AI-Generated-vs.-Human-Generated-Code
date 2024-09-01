def value_check(students, n):
    result = all(x == n for x in students.values()) 
    return result
  
students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
print("Original Dictionary:")
print(students)
n = 12
print("\nCheck all are ",n,"in the dictionary.")
print(value_check(students, n))
n = 10
print("\nCheck all are ",n,"in the dictionary.")
print(value_check(students, n))
