import requests

from bs4 import BeautifulSoup

# 검색시 나오는 사이트
req = requests.get("https://www.daangn.com/search/%EC%97%90%EC%96%B4%ED%8C%9F")
html = req.text
soup = BeautifulSoup(html, "html.parser")
my_titles = soup.select(
    '#flea-market-wrap'
)
for title in my_titles:
    print(title.text)
    #print(title.get('href'))
