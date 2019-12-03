#coding: utf-8

import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\souppt\chromedriver')
driver.get('http://browse.gmarket.co.kr/search?keyword=조각상&f=c%3A100000051&txtSrchKeyword=조각상&x=0&y=0') # 에어팟 부분 고치면 다른거 검색 가능
driver.implicitly_wait(10)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div',{'module-design-id':'15'})
name = content.find_all('span',{'class':'text__item'})
price = content.find_all('strong',{'class':'text text__value'})
	
for n, p in zip(name, price):
	print(n.get_text() + " : " + p.get_text())