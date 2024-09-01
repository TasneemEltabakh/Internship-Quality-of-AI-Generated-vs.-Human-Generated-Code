# Python3 code to illustrate the conversion of
# datetime.datetime to excel serial date number


# Importing datetime module
import datetime


# Calling the now() function to return
# current date and time
current_datetime = datetime.datetime.now()


# Calling the strftime() function to convert
# the above current datetime into excel serial date number
print(current_datetime.strftime('%x %X'))