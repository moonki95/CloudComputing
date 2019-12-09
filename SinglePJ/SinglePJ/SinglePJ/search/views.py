#!/usr/bin/env python3
from django.shortcuts import render
from urllib.request import urlretrieve
#from .models import SearchList
from django.views import generic
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


# Create your views here.

def main(request):
    template_name = 'search/main.html'
    return render(request, template_name)

def check_get(request):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_driver_path = '/home/ubuntu/chromedriver'
    driver = webdriver.Chrome(executable_path='/home/ubuntu/chromedriver', options=chrome_options)

    template_name = 'search/search.html'
    sc = request.GET.get('search', None)
    #search_list = SearchList.objects.all()
    #search_list.delete()

    try:
        driver.get('http://browse.gmarket.co.kr/search?keyword='+sc+'&f=c:100000051&txtsrchkeyword=+'+sc+'"&x=0&y=0&s=3&k=0&p=1')
        for _ in range(50):
            # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
            driver.execute_script("window.scrollBy(0,100)")
        sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        content = soup.find('div', {'module-design-id': '15'})
        name = content.find_all('span', {'class': 'text__item'})
        price = content.find_all('strong', {'class': 'text text__value'})
        del_price = content.find_all('span', {'class': 'text__tag'})
        title = content.find_all('div', {'class': 'box__item-title'})
        img = content.find_all('img',{'class':'image__item'})

    except AttributeError:
        msg = "검색 결과가 없습니다."
        return render(request, template_name, {"msg" : msg})

    link_p = []
    del_p = []
    img_src = []

    text = []


    for link in title:
        url = link.find('a', {'class': 'link__item'})
        if 'href' in url.attrs:
            link_p.append(url.attrs['href'])

    for dp in del_price:
        if "배송비" in dp.get_text():
            del_p.append(dp.get_text())

    for im in img:
        if 'src' in im.attrs:
            img_src.append(im.attrs['src'])

    for n, p, dp, l, img in zip(name, price, del_p, link_p, img_src):
        text.append([n.get_text(), p.get_text() + "원", "데이터 없음", dp, l, "G마켓", img])

    response = requests.get('https://www.daangn.com/search/'+sc)
    html = response.text
    bsobj = BeautifulSoup(html, "html.parser")

    cont = bsobj.find("div", {"class":"result-container"})
    namelist = cont.findAll("span", {"class": "article-title"})
    addresslist = cont.findAll("p", {"class": "article-region-name"})
    pricelist = cont.findAll("p", {"class": "article-price"})
    url = cont.find_all("a", {"class": "flea-market-article-link"})
    img_div = cont.find_all("div",{"class": "card-photo"})

    link_car = []
    img_s = []

    for lk in url:
        if 'href' in lk.attrs:
            link_car.append(lk.attrs['href'])

    for div in img_div:
        image = div.find("img")
        if 'src' in image.attrs:
            img_s.append(image.attrs['src'])


    for i, j, k, l, img in zip(namelist, addresslist, pricelist, link_car, img_s):
        text.append([i.get_text(), k.get_text(), j.get_text(), "데이터 없음", "https://www.daangn.com/" + l, "당근마켓", img])

    driver.get('https://nid.naver.com/nidlogin.login')
    # 아이디/비밀번호를 입력해준다.
    # driver.find_element_by_name('id').send_keys('id')
    # driver.find_element_by_name('pw').send_keys('pw')
    id = 'id'
    pw = 'password'
    driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
    driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")

    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    sleep(1)
    url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query="+sc+"&search.menuid=&search.searchBy=1&search.sortBy=date&search.clubid=10050146&search.option=0&search.defaultValue=1"
    driver.get(url)
    sleep(5)


    for j in range(1, 2):
        for i in range(1, 10):
            # prodcut_link : 상품 url
            product_link = driver.find_element_by_css_selector(
                "#articleList > ul:nth-child(%d) > li:nth-child(%d) > a"%(j, i)).get_attribute('href')
            # product_name : 상품 이름
            product_name = driver.find_element_by_css_selector(
                "#articleList > ul:nth-child(%d) > li:nth-child(%d) > a > div > div.tit > h3"%(j, i)).text
            # product_page : 상품 페이지로 가기
            product_page = driver.find_element_by_css_selector(
                "#articleList > ul:nth-child(%d) > li:nth-child(%d) > a"%(j, i)).click()
            sleep(5)
            try:
                driver.find_element_by_class_name('tran_type')
                product_price = driver.find_element_by_class_name('price').text

            except:
                i = i + 1
                driver.back()
                continue
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            img_j = soup.find("img")
            if 'src' in img_j.attrs:
                text.append([product_name, product_price, "테이터 없음", "데이터 없음", product_link, "중고나라", img_j.attrs['src']])

            driver.back()
        # product_more : 더보기 기능
        product_more = driver.find_element_by_css_selector("#moreButtonArea > div").click()

    return render(request, template_name,{"text" : text})
