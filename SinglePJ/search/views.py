from django.shortcuts import render
from .models import SearchList
from django.views import generic
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# Create your views here.

def main(request):
    template_name = 'search/main.html'
    return render(request, template_name)

def check_get(request):
    template_name = 'search/search.html'
    sc = request.GET.get('search', None)
    search_list = SearchList.objects.all()
    search_list.delete()

    #driver = webdriver.Chrome('C:\souppt\chromedriver')
    #driver.get( 'http://browse.gmarket.co.kr/search?keyword='+sc+'&f=c:100000051&txtsrchkeyword='+sc+'&x=0&y=0&s=3&k=0&p=1')
    #driver.implicitly_wait(3)

    response = requests.get('http://browse.gmarket.co.kr/search?keyword='+sc+'&f=c:100000051&txtsrchkeyword=+'+sc+'"&x=0&y=0&s=3&k=0&p=1')

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', {'module-design-id': '15'})
    name = content.find_all('span', {'class': 'text__item'})
    price = content.find_all('strong', {'class': 'text text__value'})
    del_price = content.find_all('span', {'class': 'text__tag'})
    title = content.find_all('div', {'class': 'box__item-title'})
    link_p = []
    del_p = []

    for link in title:
        url = link.find('a', {'class': 'link__item'})
        if 'href' in url.attrs:
            link_p.append(url.attrs['href'])

    for dp in del_price:
        if "배송비" in dp.get_text():
            del_p.append(dp.get_text())

    for n, p, dp, l in zip(name, price, del_p, link_p):
        slist = SearchList()
        slist.name = n.get_text()
        slist.price = p.get_text() + "원"
        slist.del_price = dp
        slist.url = l
        slist.site = "G마켓"
        slist.save()

    response = requests.get('https://www.daangn.com/search/'+sc)
    html = response.text
    bsobj = BeautifulSoup(html, "html.parser")

    cont = bsobj.find("div", {"class":"result-container"})
    namelist = cont.findAll("span", {"class": "article-title"})
    addresslist = cont.findAll("p", {"class": "article-region-name"})
    pricelist = cont.findAll("p", {"class": "article-price"})
    url = cont.find_all("a", {"class": "flea-market-article-link"})
    link_car = []

    for lk in url:
        if 'href' in lk.attrs:
            link_car.append(lk.attrs['href'])


    for i, j, k, l in zip(namelist, addresslist, pricelist, link_car):
        slist = SearchList()
        slist.name = i.get_text()
        slist.place = j.get_text()
        slist.price = k.get_text()
        slist.url = "https://www.daangn.com/" + l
        slist.site = "당근마켓"
        slist.save()

    return render(request, template_name,{"search_list": search_list})