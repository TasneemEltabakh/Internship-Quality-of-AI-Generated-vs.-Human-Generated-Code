# Importing required modules
import csv
from datetime import datetime


# Here we are storing our data in a
# variable. We'll add this data in
# our csv file
rows = [['GeeksforGeeks1', 'GeeksforGeeks2'],
['GeeksforGeeks3', 'GeeksforGeeks4'],
['GeeksforGeeks5', 'GeeksforGeeks6']]

# Opening the CSV file in read and
# write mode using the open() module
with open(r'YOUR_CSV_FILE.csv', 'r+', newline='') as file:

# creating the csv writer
file_write = csv.writer(file)

# storing current date and time
current_date_time = datetime.now()

# Iterating over all the data in the rows
# variable
for val in rows:

# Inserting the date and time at 0th
# index
val.insert(0, current_date_time)

# writing the data in csv file
file_write.writerow(val)