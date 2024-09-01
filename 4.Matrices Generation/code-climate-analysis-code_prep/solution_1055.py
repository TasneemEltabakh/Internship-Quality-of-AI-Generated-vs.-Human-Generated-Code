import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("First four h2 tags from the webpage python.org.:")
print(soup.find_all('a')[0:10])

