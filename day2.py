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
    html2 = requests.get(article_url).text
    article_soup = BeautifulSoup(html2, 'html.parser')

    #어떤 물품들을 로그인을 해야지 상품 페이지에 접속하여 price를 가져올 수 있다.
    #페이지 접속을 못 해 에러나는 상품들은 None으로 처리했다.

    try:
        price = article_soup.select('.product_name.price')[0].text
    except IndexError:
        price = None
    print(price)
