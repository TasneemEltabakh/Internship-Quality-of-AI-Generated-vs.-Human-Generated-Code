# Python program to verify IP without using RegEx


# explicit function to verify IP
def isValidIP(s):


# check number of periods
if s.count('.') != 3:
return 'Invalid Ip address'


l = list(map(str, s.split('.')))


# check range of each number between periods
for ele in l:
if int(ele) < 0 or int(ele) > 255:
return 'Invalid Ip address'


return 'Valid Ip address'




# Driver Code
print(isValidIP('666.1.2.2'))