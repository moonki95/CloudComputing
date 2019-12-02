import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

list_url = 'https://m.cafe.naver.com/ArticleAllListAjax.nhn'

params = {
    'search.clubid' : 'wjdalsrbekt',# id
    'search.menuid': '1768',  # 가방/모자/장갑 게시판
    'search.boardtype': 'L',  #
    'search.questionTab': 'A',
    'search.totalCount': '201',
    'search.page': 1,
}
html = requests.get(list_url, params=params).text
soup = BeautifulSoup(html, 'html.parser')

for tag in soup.select('li'):
    article_url = urljoin(list_url, tag.find('a')['href'])  # 맨 처음 에 있는 a항목을 가져온다.
    article_title = tag.find(class_='tit').text.strip()
    print(article_title, article_url)

    html2 = requests.get(article_url).text
    article_soup = BeautifulSoup(html2, 'html.parser')

                            # 어떤 물품들을 로그인을 해야지 가격정보를 알려준다.
                                # 가격이 없어 에러나는 부분은 None 으로 처리했다.

    try:
        price = article_soup.select('.product_name.price')[0].text
    except IndexError:
        price = None
    print(price)