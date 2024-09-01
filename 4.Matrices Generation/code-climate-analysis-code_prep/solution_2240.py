# importing necessary packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# for holding the resultant list
element_list = []

for page in range(1, 3, 1):

page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(page_url)
title = driver.find_elements_by_class_name("title")
price = driver.find_elements_by_class_name("price")
description = driver.find_elements_by_class_name("description")
rating = driver.find_elements_by_class_name("ratings")

for i in range(len(title)):
element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)

#closing the driver
driver.close()