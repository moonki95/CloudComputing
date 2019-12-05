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
        slist.price = p.get_text()
        slist.del_price = dp
        slist.url = l
        slist.site = "G마켓"
        slist.save()

    return render(request, template_name,{"search_list": search_list})
