from bs4 import BeautifulSoup
html_content = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_content, "lxml")
print("Original Markup:")
print(soup.a)
tag = soup.a
tag = tag.clear()
print("\nAfter clearing the contents in the tag:")
print(soup.a)
