# Python3 code to demonstrate
# Getting datetime object using a date_string

# importing datetime module
import datetime

# datestring for which datetime_obj required
date_string = '2021-09-01 15:27:05.004573 +0530'
print("string datetime: ")
print(date_string)
print("datestring class is :", type(date_string))

# using strptime() to get datetime object
datetime_obj = datetime.datetime.strptime(
date_string, '%Y-%m-%d %H:%M:%S.%f %z')

print("converted to datetime:")

# Printing datetime
print(datetime_obj)

# Checking class of datetime_obj.
print("datetime_obj class is :", type(datetime_obj))