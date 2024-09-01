from bs4 import BeautifulSoup
html_markup= '<a href="https://w3resource.com/">Python exercises<i>w3resource</i></a>'
soup = BeautifulSoup(html_markup, "lxml")
print("Original markup:")
a_tag = soup.a
print(a_tag)
new_tag = soup.new_tag("b")
new_tag.string = "PHP"
b_tag = a_tag.i.replace_with(new_tag)
print("New Markup:")
print(a_tag)
