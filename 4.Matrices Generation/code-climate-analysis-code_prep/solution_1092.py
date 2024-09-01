import requests
url = 'http://httpbin.org/cookies'
# A dictionary (my_cookies) of cookies to send to the specified url.
my_cookies = dict(cookies_are='Cookies parameter use to send cookies to the server')
r = requests.get(url, cookies = my_cookies)
print(r.text)
# Accessing cookies with Requests
# url = 'http://WebsiteName/cookie/setting/url'
# res = requests.get(url)
# Value of cookies
# print(res.cookies['cookie_name'])
