from bs4 import BeautifulSoup
html_content = '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_content, "lxml")
print("Original Markup:")
print(soup.a)
i_tag = soup.i.extract()
print("\nExtract i tag from said html Markup:")
print(i_tag)
