import csv

# creating a nested list of roll numbers,
# subjects and marks scored by each roll number
marks = [
["RollNo", "Maths", "Python"],
[1000, 80, 85],
[2000, 85, 89],
[3000, 82, 90],
[4000, 83, 98],
[5000, 82, 90]
]

# using the open method with 'w' mode
# for creating a new csv file 'my_csv' with .csv extension
with open('my_csv.csv', 'w', newline = '') as file:
writer = csv.writer(file, quoting = csv.QUOTE_NONNUMERIC,
delimiter = ' ')
writer.writerows(marks)

# opening the 'my_csv' file to read its contents
with open('my_csv.csv', newline = '') as file:

reader = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC,
delimiter = ' ')

# storing all the rows in an output list
output = []
for row in reader:
output.append(row[:])

for rows in output:
print(rows)