# import datetime module
import datetime

# convert datetime to epoch using strftime from
# time stamp 2021/7/7/1/2/1
# for linux:
epoch = datetime.datetime(2021, 7, 7, 1, 2, 1).strftime('%s')
# for windows:
# epoch = datetime.datetime(2021, 7,7 , 1,2,1).strftime('%S')
print(epoch)

# convert datetime to epoch using strftime from
# time stamp 2021/3/3/4/3/4
epoch = datetime.datetime(2021, 3, 3, 4, 3, 4).strftime('%s')
print(epoch)

# convert datetime to epoch using strftime from
# time stamp 2021/7/7/12/12/34
epoch = datetime.datetime(2021, 7, 7, 12, 12, 34).strftime('%s')
print(epoch)

# convert datetime to epoch using strftime from
# time stamp 2021/7/7/12/56/00
epoch = datetime.datetime(2021, 7, 7, 12, 56, 0).strftime('%s')
print(epoch)