import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
list_url = 'https://m.cafe.naver.com/joonggonara'

html = requests.get(list_url).text
soup = BeautifulSoup(html,'html.parser')

#select는 해당 조건을 만족시키는 다수를 찾는것이고,
#find는 해당 조건을 만족시키는 첫번째 것을 찾아낸다.

for tag in soup.select('#articleListArea li'):
    article_url = urljoin(list_url,tag.find('a')['href'])#맨 처음에 있는 a항목을 가져온다.
    article_title = tag.find(class_='tit').text.strip()
    print(article_title, article_url)