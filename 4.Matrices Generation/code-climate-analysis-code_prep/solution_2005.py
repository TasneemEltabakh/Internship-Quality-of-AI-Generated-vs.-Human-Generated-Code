import re

def convert_phone_number(phone):

# actual pattern which only change this line
num = re.sub(r'(?<!\S)(\d{3})-', r'(\1) ', phone)
return num

# Driver code
print(convert_phone_number("Call geek 321-963-0612"))