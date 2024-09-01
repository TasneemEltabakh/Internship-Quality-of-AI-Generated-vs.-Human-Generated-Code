# import os library
import os


# infinite while loop
while True:
print("Hello! user choose your tool")
print("Choose your tool :-\n")
print("-> mousepad")
print("-> chrome")
print("-> vlc")
print("-> virtualbox")
print("-> camera")
print("-> telegram")
print("-> firefox")
print("-> codeblocks")
print("-> screenshot")
print("-> task-manager")
print("-> libreoffice impress / presentation")
print("-> libreoffice writer / text editor / notepad")
print("-> libreoffice clac / spreadsheets")
print("-> libreoffice")
print("-> jupyter notebook\n")
print("chat with system:-",end=' ')

# take input from user
p = input()

# check conditions
if (("do not" in p) or ("dont" in p) or ("don't" in p)):
print("OK user\n")

elif (("open" in p) or ("start" in p) or ("run" in p) or ("execute" in p) or ("launch" in p) or ("activate" in p)):

if (("mousepad" in p) or ("editor" in p)):

# run mention application
os.system("mousepad")

elif (("vlc" in p) or ("media player" in p)):
os.system("vlc")

elif (("virtualbox" in p) or ("virtual machine" in p) or ("virtual tool" in p)):
os.system("virtualbox")

elif (("camera" in p) or ("cheese" in p)):
os.system("cheese")

elif ("telegram" in p):
os.system("telegram-desktop")

elif ("codeblocks" in p):
os.system("codeblocks")

elif ("taskmanager" in p):
os.system("xfce4-taskmanager")

elif ("screenshot" in p):
os.system("xfce4-screenshooter")

elif (("jupyter" in p) or ("notebook" in p)):
os.system("jupyter notebook")

elif (("libreoffice impress" in p) or ("presentation tool" in p)):
os.system("libreoffice --impress")

elif (("libreoffice writer" in p) or ("text editor" in p)):
os.system("libreoffice --writer")


elif ("notepad" in p):
os.system("notepad")

elif (("libreoffice calc" in p) or ("spreadsheet" in p)):
os.system("libreoffice --calc")

elif ("libreoffice" in p):
os.system("libreoffice")

elif ("chrome" in p):
os.system("google-chrome-stable")

elif (("firefox" in p) or ("mozilla" in p)):
os.system("firefox")

else :
print("don't support")

# terminating infinite while loop
elif (("quit" in p) or ("exit" in p) or ("stop" in p) or ("close" in p) or ("deactivate" in p) or ("terminate" in p)):
print("Thnank You!")
break

else :
print("don't support")