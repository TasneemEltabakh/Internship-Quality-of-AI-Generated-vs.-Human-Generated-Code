import csv
reader = csv.reader(open("employees.csv"))
for row in reader:
    print(row)
