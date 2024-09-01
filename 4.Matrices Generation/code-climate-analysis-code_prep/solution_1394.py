import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nNames of all HTML tags (https://www.python.org):\n")
for child in soup.recursiveChildGenerator():
    if child.name:
        print(child.name)

