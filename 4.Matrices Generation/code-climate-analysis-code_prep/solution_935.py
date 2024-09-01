import requests
from bs4 import BeautifulSoup
url = 'https://www.w3resource.com/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nFind and print all li tags:\n")
for tag in soup.find_all("li"):
    print("{0}: {1}".format(tag.name, tag.text))
