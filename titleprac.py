import requests
from bs4 import BeautifulSoup

res = requests.get('http://daangn.com')


soup = BeautifulSoup(res.content, 'html.parser')
title = soup.find('title')
print(title.get_text())

