import csv

# reading data from a csv file 'Data.csv'
with open('Data.csv', newline='') as file:

reader = csv.reader(file, delimiter = ' ')

# store the headers in a separate variable,
# move the reader object to point on the next row
headings = next(reader)

# output list to store all rows
Output = []
for row in reader:
Output.append(row[:])

for row_num, rows in enumerate(Output):
print('data in row number {} is {}'.format(row_num+1, rows))

print('headers were: ', headings)