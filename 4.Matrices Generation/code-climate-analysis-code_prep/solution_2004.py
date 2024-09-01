# Python3 code to demonstrate working of
# Last weekday of every month in year
# Using loop + max() + calendar.monthcalendar
import calendar

# initializing year
year = 1997

# printing Year
print("The original year : " + str(year))

# initializing weekday
weekdy = 5

# iterating for all months
res = []
for month in range(1, 13):

# max gets last friday of each month of 1997
res.append(str(max(week[weekdy]
for week in calendar.monthcalendar(year, month))) +
"/" + str(month)+ "/" + str(year))

# printing
print("Last weekdays of year : " + str(res))