# for using os.popen()
import os


# sending the uptime command as an argument to popen()
# and saving the returned result (after truncating the trailing \n)
t = os.popen('uptime -p').read()[:-1]


print(t)