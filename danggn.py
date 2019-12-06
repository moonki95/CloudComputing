from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.daangn.com/search/%EC%97%90%EC%96%B4%ED%8C%9F')
bsobj = BeautifulSoup(html,"html.parser")

namelist = bsobj.findAll("span", {"class":"article-title"})
addresslist = bsobj.findAll("p",{"class" :"article-region-name"})
pricelist = bsobj.findAll("p",{"class" : "article-price"})

for i,j,k in zip(namelist, addresslist, pricelist):
    print(i.get_text() + j.get_text() + k.get_text())

