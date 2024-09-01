# Import Library
from selenium import webdriver
import time

# set webdriver path here it may vary
# Its the location where you have downloaded the ChromeDriver
driver = webdriver.Chrome(executable_path=r"C:\\chromedriver.exe")

# Get the target URL
driver.get('https://html.com/tags/button/')

# Wait for 5 seconds to load the webpage completely
time.sleep(5)

# Find the button using text
driver.find_element_by_xpath('//button[normalize-space()="Click me!"]').click()

time.sleep(5)

# Close the driver
driver.close()