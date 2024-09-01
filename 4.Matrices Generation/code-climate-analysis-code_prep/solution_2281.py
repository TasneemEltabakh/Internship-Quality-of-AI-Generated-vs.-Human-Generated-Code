# importing datetime module
from datetime import datetime

# Getting today's date
todays_Date = datetime.now()

# Get date into the isoformat
isoformat_date = todays_Date.isoformat()

# print the type of date
print(type(isoformat_date))

# convert string date into datetime format
result = datetime.fromisoformat(isoformat_date)
print(type(result))