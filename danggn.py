from urllib.request import urlopen
from bs4 import BeautifulSoup

def crawling():
    html = urlopen('https://www.daangn.com/search/%EC%97%90%EC%96%B4%ED%8C%9F')
    bsobj = BeautifulSoup(html, "html.parser")
    link=[]
    cont = bsobj.find("div", {"class": "result-container"})
    namelist = cont.findAll("span", {"class": "article-title"})
    addresslist = cont.findAll("p", {"class": "article-region-name"})
    pricelist = cont.findAll("p", {"class": "article-price"})
    hyperlink = bsobj.findAll("a", {"class" : "flea-market-article-link"})

    for hyperl in hyperlink:
        if 'href' in hyperl.attrs:
            link.append(hyperl.attrs['href'])

    for i,j,k,l in zip(namelist, addresslist, pricelist, hyperlink):
        print(i.get_text() + j.get_text() + k.get_text() + '' +l.get_text())

crawling()
