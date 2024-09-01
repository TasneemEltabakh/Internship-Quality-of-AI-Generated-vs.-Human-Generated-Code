import csv
f = open("employees.csv", "r")
reader = csv.reader(f)
next(reader)

for row in reader:
    print(row)
