# Python3 code to demonstrate working of
# Convert date range to N equal durations
# Using loop
import datetime

# initializing dates
test_date1 = datetime.datetime(1997, 1, 4)
test_date2 = datetime.datetime(1997, 1, 30)

# printing original dates
print("The original date 1 is : " + str(test_date1))
print("The original date 2 is : " + str(test_date2))

# initializing N
N = 7

temp = []

# getting diff.
diff = ( test_date2 - test_date1) // N
for idx in range(0, N):

# computing new dates
temp.append((test_date1 + idx * diff))

# using strftime to convert to userfriendly
# format
res = []
for sub in temp:
res.append(sub.strftime("%Y/%m/%d %H:%M:%S"))

# printing result
print("N equal duration dates : " + str(res))