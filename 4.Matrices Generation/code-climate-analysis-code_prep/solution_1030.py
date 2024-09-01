from bs4 import BeautifulSoup
str1 = "<p>Some<b>bad<i>HTML Code</i></b></p>"
print("Original string:")
print(str1)
soup = BeautifulSoup("<p>Some<b>bad<i>HTML Code</i></b></p>", "xml")
print("\nFormatted Unicode string:")
print(soup.prettify())
