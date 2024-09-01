# Python3 code to demonstrate working of
# Group dates in K ranges
# Using groupby() + sort()
from itertools import groupby
from datetime import datetime

# initializing list
test_list = [datetime(2020, 1, 4),
datetime(2019, 12, 30),
datetime(2020, 1, 7),
datetime(2019, 12, 27),
datetime(2020, 1, 20),
datetime(2020, 1, 10)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 7

# initializing start date
min_date = min(test_list)

# utility fnc to form groupings
def group_util(date):
return (date-min_date).days // K

# sorting before grouping
test_list.sort()

temp = []
# grouping by utility function to group by K days
for key, val in groupby(test_list , key = lambda date : group_util(date)):
temp.append((key, list(val)))

# using strftime to convert to userfriendly
# format
res = []
for sub in temp:
intr = []
for ele in sub[1]:
intr.append(ele.strftime("%Y/%m/%d"))
res.append((sub[0], intr))

# printing result
print("Grouped Digits : " + str(res))