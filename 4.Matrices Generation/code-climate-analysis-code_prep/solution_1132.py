import os
fd = os.open( "/tmp", os.O_RDONLY )
os.fchown( fd, 100, -1)
os.fchown( fd, -1, 50)
print("Changed ownership successfully..")
os.close( fd )
