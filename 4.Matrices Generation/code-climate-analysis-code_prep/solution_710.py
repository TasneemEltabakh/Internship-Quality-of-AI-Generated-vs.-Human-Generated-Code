import csv
csv.register_dialect('csv_dialect',
                    delimiter='|',
                    skipinitialspace=True,
                    quoting=csv.QUOTE_ALL)
with open('temp.csv', 'r') as csvfile:
   reader = csv.reader(csvfile, dialect='csv_dialect')
   for row in reader:
       print(row)
