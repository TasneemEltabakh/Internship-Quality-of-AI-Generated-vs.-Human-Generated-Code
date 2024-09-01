# importing the module
import os

# sets the text colour to green
os.system("tput setaf 2")

print("Launching Terminal User Interface")

# sets the text color to red
os.system("tput setaf 1")

print("\t\tWELCOME TO Terminal User Interface\t\t\t")

# sets the text color to white
os.system("tput setaf 7")

print("\t-------------------------------------------------")
print("Entering local device")
while True:
print("""
1.Print date
2.Print cal
3.Configure web
4.Configure docker
5.Add user
6.Delete user
7.Create a file
8.Create a folder
9.Exit""")

ch=int(input("Enter your choice: "))

if(ch == 1):
os.system("date")

elif ch == 2:
os.system("cal")

elif ch == 3:
os.system("yum install httpd -y")
os.system("systemctl start httpd")
os.system("systemctl status httpd")

elif ch == 4:
os.system("yum install docker-ce -y")
os.system("systemctl start docker")
os.system("systemctl status docker")


elif ch == 5:
new_user=input("Enter the name of new user: ")
os.system("sudo useradd {}".format(new_user))
os.system("id -u {}".format(new_user) )

elif ch == 6:
del_user=input("Enter the name of the user to delete: ")
os.system("sudo userdel {}".format(del_user))

elif ch == 7:
filename=input("Enter the filename: ")
f=os.system("sudo touch {}".format(filename))
if f!=0:
print("Some error occurred")
else:
print("File created successfully")

elif ch == 8:
foldername=input("Enter the foldername: ")
f=os.system("sudo mkdir {}".format(foldername))
if f!=0:
print("Some error occurred")
else:
print("Folder created successfully")

elif ch == 9:
print("Exiting application")
exit()
else:
print("Invalid entry")

input("Press enter to continue")
os.system("clear")