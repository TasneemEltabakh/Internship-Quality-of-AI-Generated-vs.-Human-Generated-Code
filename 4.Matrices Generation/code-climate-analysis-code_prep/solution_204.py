from bs4 import BeautifulSoup
html_doc = '<a href="http://example.com/">HTML<i>w3resource.com</i></a>'
soup = BeautifulSoup(html_doc, "lxml")
print("\nOriginal Markup:")
print(soup.a)
soup.a.append("CSS")
print("\nAfter append a text in the new link:")
print(soup.a)
