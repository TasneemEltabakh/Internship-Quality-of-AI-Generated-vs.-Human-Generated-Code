from bs4 import BeautifulSoup
soup = BeautifulSoup("<b>w3resource.com</b>", "lxml")
print("Original Markup:")
print(soup.b)
tag = soup.new_tag("i")
tag.string = "Python"
print("\nNew Markup, after inserting the text:")
soup.b.string.insert_after(tag)
print(soup.b)
