# Import the required modules
from selenium import webdriver
import time

# Main Function
if __name__ == '__main__':

# Provide the email and password
email = ''
password = ''

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Provide the path of chromedriver
# present on your system.
driver = webdriver.Chrome(
executable_path="C:/chromedriver/chromedriver.exe",
chrome_options=options)
driver.set_window_size(1920, 1080)

# Send a get request to the url
driver.get('https://auth.geeksforgeeks.org/')
time.sleep(5)

# Finds the input box by name
# in DOM tree to send both
# the provided email and password in it.
driver.find_element_by_name('user').send_keys(email)
driver.find_element_by_name('pass').send_keys(password)

# Find the signin button and click on it.
driver.find_element_by_css_selector(
'button.btn.btn-green.signin-button').click()
time.sleep(5)

# Returns the list of elements
# having the following css selector.
container = driver.find_elements_by_css_selector(
'div.mdl-cell.mdl-cell--9-col.mdl-cell--12-col-phone.textBold')

# Extracts the text from name,
# institution, email_id css selector.
name = container[0].text
try:
institution = container[1].find_element_by_css_selector('a').text
except:
institution = container[1].text
email_id = container[2].text

# Output
print({"Name": name, "Institution": institution,
"Email ID": email})

# Quits the driver
driver.quit()