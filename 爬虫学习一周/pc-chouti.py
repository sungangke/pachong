import requests
from bs4 import BeautifulSoup

r1 = requests.get("https://dig.chouti.com/")
s1 = BeautifulSoup(r1.text,'html.parser')
r1_cookie = r1.cookies.get_dict()

"""
phone: 86wew
password: we
oneMonth: 1
"""
r2 = requests.post(
    'https://dig.chouti.com/login',
    data={
      'phone':'13311213092',
        'password':'123456789',
        'oneMonth':1
    },
    cookies=r1_cookie
)
r2_cookie = r2.cookies.get_dict()
cookie_dict = {}
cookie_dict.update(r1_cookie)
cookie_dict.update(r2_cookie)

r3 = requests.post('https://dig.chouti.com/link/vote?linksId=23579106',cookies=cookie_dict)
# print(r3.text)
