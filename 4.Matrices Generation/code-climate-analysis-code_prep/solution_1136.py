import csv
print("\nWith initial spaces after a delimiter:\n")
with open('departments.csv', 'r') as csvfile:
   data = csv.reader(csvfile, skipinitialspace=False)
   for row in data:
     print(', '.join(row))
print("\n\nWithout initial spaces after a delimiter:\n")
with open('departments.csv', 'r') as csvfile:
   data = csv.reader(csvfile, skipinitialspace=True)
   for row in data:
     print(', '.join(row))
