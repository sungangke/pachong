import requests
from bs4 import BeautifulSoup

r1 = requests.get("https://github.com/login")
s1 = BeautifulSoup(r1.text,'html.parser')
token = s1.find(name='input',attrs={'name':'authenticity_token'}).get('value')
r1_cookies = r1.cookies.get_dict()

r2 = requests.post("https://github.com/session",
                   data={
                       'utf-8':'✓',
                       'authenticity_token':'token',
                       'login':'xxx', #登录的用户名
                       'password':'*******', #登录的用户密码
                       'commit':'Sign in'
                   },
                   cookies=r1_cookies
                   )

cookies_dict={}
cookies_dict.update(r1_cookies)
cookies_dict.update(r2.cookies.get_dict())

r3 = requests.get(
    url="https://github.com/sungangke/pachong",cookies=cookies_dict)
print(r3.text)