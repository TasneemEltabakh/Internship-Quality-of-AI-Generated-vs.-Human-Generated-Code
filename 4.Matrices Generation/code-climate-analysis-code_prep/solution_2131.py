import urllib.request
from bs4 import BeautifulSoup

# here we have to pass url and path
# (where you want to save ur text file)
urllib.request.urlretrieve("https://www.geeksforgeeks.org/grep-command-in-unixlinux/?ref=leftbar-rightbar",
"/home/gpt/PycharmProjects/pythonProject1/test/text_file.txt")

file = open("text_file.txt", "r")
contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')

f = open("test1.txt", "w")

# traverse paragraphs from soup
for data in soup.find_all("p"):
sum = data.get_text()
f.writelines(sum)

f.close()