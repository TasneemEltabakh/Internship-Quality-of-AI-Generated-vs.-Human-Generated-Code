import csv
reader = csv.reader(open("employees.csv"))
no_lines= len(list(reader))
print(no_lines)
