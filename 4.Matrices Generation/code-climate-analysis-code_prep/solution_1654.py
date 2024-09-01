import arrow
from datetime import datetime
from dateutil import tz
print("\nCreate a date from a given date and a given time zone:")
d1 = arrow.get(datetime(2018, 7, 5), 'US/Pacific')
print(d1)
print("\nCreate a date from a given date and a time zone object from a string representation:")
d2 = arrow.get(datetime(2017, 7, 5), tz.gettz('America/Chicago'))
print(d2)
d3 = arrow.get(datetime.now(tz.gettz('US/Pacific')))
print("\nCreate a date using current datetime and a specified time zone:")
print(d3)
