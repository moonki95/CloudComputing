import urllib.request
from urllib.request import urlretrieve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

import time

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_driver_path = 'C:\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
url = "https://m.cafe.naver.com/ArticleSearchList.nhn?search.query=%EC%95%84%EC%9D%B4%ED%8F%B0&search.menuid=&search.searchBy=1&search.sortBy=date&search.clubid=10050146&search.option=0&search.defaultValue=1"
driver.get(url)

sleep(5)

h1 = driver.find_element_by_css_selector("#articleList > ul > li:nth-child(1) > a").click()
sleep(5)
selected_class=driver.find_element_by_class_name('price').text
print(selected_class)
