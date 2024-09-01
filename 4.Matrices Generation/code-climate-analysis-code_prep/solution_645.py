from bs4 import BeautifulSoup
markup = '<a href="https://w3resource.com/">Python exercises.<i>w3resource.com</i></a>'
soup = BeautifulSoup(markup, "lxml")
a_tag = soup.a
print("Original markup:")
print(a_tag)
a_tag.i.unwrap()
print("\nAfter unwrapping:")
print(a_tag)
