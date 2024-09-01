from bs4 import BeautifulSoup
soup = BeautifulSoup("<b>w3resource.com</b>", "lxml")
print("Original Markup:")
print(soup.b)
tag = soup.new_tag("i")
tag.string = "Python"
print("\nNew Markup, before inserting the text:")
soup.b.string.insert_before(tag)
print(soup.b)
