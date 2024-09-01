# Python program to illustrate the
# convertion of unix timestamp string
# to its readable date


# Importing datetime module
import datetime


# Calling the fromtimestamp() function to
# extract datetime from the given timestamp


# Calling the strftime() function to convert
# the extracted datetime into its string format
print(datetime.datetime.fromtimestamp(int("1294113662"))
.strftime('%Y-%m-%d %H:%M:%S'))